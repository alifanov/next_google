import re
from pprint import pprint
import json
import time
import getpass
import smtplib
from email.mime.text import MIMEText

to_addr = 'al@rating.vc'

message = """From: HH <{}>
To: To Rating.VC <{}>
Subject: Ask about vacancy

Just ask. Email: {}
"""


def validateEmail(email):

    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    return False

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
print '>>> input_data = '
pprint(in_data, indent=4)
time.sleep(3)
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
print '>>> {}'.format(work_def)
time.sleep(3)
print '>>> work(input_data)'
for i,g in enumerate(goods):
    print '[{}]: {}'.format(i, g)
    time.sleep(1)

ans = None
while not ans:
    a = raw_input('\n\nDo you want to send your CV ? (Y/n)')
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
                smtpObj.sendmail(getpass.getuser(), [email,], to_addr, message.format(getpass.getuser(), email))
                print "Successfully sent email"
            except smtplib.SMTPException:
                print "Error: unable to send the email"
                print "Send your CV to {}".format(to_addr)
        else:
            print 'Wrong e-mail format. Try once more.'