from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import time
import schedule

def mail():

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pczone.devlops@gmail.com', 'byfu mqyo oybp hzbj')

    msg = MIMEMultipart()
    msg['Subject'] = "Namaskar Master, Email sender Automation Script by Piyush Chitte"

    to = ['marvellousinfosystem@gmail.com']
    smtp.sendmail(from_addr = "pczone.devlops@gmail.com", to_addrs = to,msg = msg.as_string())

schedule.every(2).minutes.do(mail)

while True:
    schedule.run_pending()
    time.sleep(1)