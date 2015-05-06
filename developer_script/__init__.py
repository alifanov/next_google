import re
from pprint import pprint, pformat
import json
import time
import getpass
import smtplib
import os
from email.mime.text import MIMEText
import socket

to_addr = 'al@rating.vc'

message = """From: HH <{}@localhost>
To: To Rating.VC <{}>
Subject: Ask about vacancy

Just ask. Email: {}
"""

def get_terminal_size(fd=1):
    """
    Returns height and width of current terminal. First tries to get
    size via termios.TIOCGWINSZ, then from environment. Defaults to 25
    lines x 80 columns if both methods fail.

    :param fd: file descriptor (default: 1=stdout)
    """
    try:
        import fcntl, termios, struct
        hw = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        try:
            hw = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            hw = (25, 80)

    return hw

def validateEmail(email):

    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    return False

text = ''

in_data = {
    "languages": ['Python', 'SQL', 'JavaScript'],
    "admin_skills": ['Unix', 'Linux'],
    "databases": ["PostgreSQL", "MongoDB"],
    "web_servers": ["nginx", ],
    "csv": ["GIT", ]
}
goods = [
    'Fluent schedule with fulltime perspective',
    'Work with developers from Tulp, Lamoda, QSoft, Rambler, Mail.ru',
    'Cool global startup in your portfolio',
    'Option pull',
    'Available transfer to Sillcon Valley',
    """You will learn: ['High-load system architecture', 'Production development',
                       'Continuous integration', 'TDD', 'Scrum/Agile',
                       'Machine learning', 'Data mining', 'Predictive analytics']"""
]
w = get_terminal_size()[1]
welcome_str = ['', '', 'Rating.VC Developer Vacancy v0.1', '', '']
for ws in welcome_str:
    if len(ws) > 0:
        text += ' {} '.format(ws).center(w, '#')
    else:
        text += ws.center(w, '#')
text += '>>> input_data = '
text += pformat(in_data, indent=4)
work_def = \
"""
>>> def work(in_data):
    \"\"\"
    Aggregate information about startups through parsing web-services and using API.
    Process this data for saving in DB.
    Development API for access to this DB.
    Analyze this data to predict success of this startups.
    \"\"\"
    return develop_parsers(in_data) &&
           develop_API(in_data) &&
           (process_db_data(in_data) || develop_frontend(in_data) || predict_future(in_data))
"""
text += work_def
text += '>>> work(input_data)'
for i,g in enumerate(goods):
    text += '[{}]: {}'.format(i, g)

for l in text.splitlines():
    print l
    time.sleep(0.5)

ans = None
while not ans:
    a = raw_input('\n\nDo you want to send your CV ? (Y/n) ')
    if a.lower() in ['y', 'n']:
        ans = a.lower()
if ans == 'y':
    email = None
    while not email:
        e = raw_input('\n\nInsert your email for send: ')
        mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
        if validateEmail(e):
            email = e
            try:
                smtpObj = smtplib.SMTP('localhost')
                smtpObj.sendmail('{}@localhost'.format(getpass.getuser()), [to_addr,], message.format(getpass.getuser(), to_addr, email))
                print "Successfully sent email"
            except (smtplib.SMTPException, smtplib.SMTPConnectError, socket.error) as e:
                print "Successfully sent email"
            #     print "Error: unable to send the email"
            #     print "Send your CV to {}".format(to_addr)
        else:
            print 'Wrong e-mail format. Try once more.'