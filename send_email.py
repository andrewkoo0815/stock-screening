#!/usr/bin/python
# Andrew sendEmail.py Version 1.0
# Created April 8, 2014
# Updated April 8, 2014

import keyring
import smtplib  
import time
import os

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

# Send email with the csv attachment to myself
def send_email(updated_list, star_list):
    if len(updated_list) == 0:
        string_list1 = "None"
    else:
        string_list1 = ", ".join(updated_list)
    if len(star_list) == 0:
        string_list2 = "None"
    else:
        string_list2 = ", ".join(star_list)
    fromaddr = 'Andrew Koo <andrewkoo@gmail.com>'
    toaddr = ['Andrew Koo <andrewkoo@gmail.com>']
    subject = 'Biotech Stock Tracker ' + time.strftime("%b %d, %Y")
    text = 'This is an automatically generated email to track your biotech stocks! Please see the csv file attached.\n\
    \n\
    - The following stocks have updated financial statement: ' + string_list1 + '\n\
    - The following updated stocks have strong revenue growth: ' + string_list2
    files = ['Files/stock_data_'+ time.strftime("%Y%m%d") + '.csv']

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = COMMASPACE.join(toaddr)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)
    
    # Credentials (if needed)  
    username = 'andrewkoo'  
    password = str(keyring.get_password("?????", "?????"))
  
    # The actual mail sent  
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()  
    server.starttls()
    server.ehlo()  
    server.login(username, password)  
    server.sendmail(fromaddr, toaddr, msg.as_string())  
    server.quit()
 
