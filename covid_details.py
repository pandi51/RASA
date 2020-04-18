import email

import requests
import smtplib

import json


def mail_send(name, mail, city):
    url = "https://api.covid19india.org/state_district_wise.json"

    res = requests.get(url)
    if(res.ok):
        tb =json.load(res.json())
        emailId = "XXXXX@gmail.com"
        pwd = "uygtyhdhnyropndf"
        # print(tb)
        msg = email.message.Message()
        msg['Subject'] = "Python Test mail"
        msg['From'] = email
        msg['To'] = mail

        msg.add_header('Content-Type', 'application/json')
        msg.set_payload(payload=str(tb))
        # msg.set_payload(payload=tb)

        smtp_obj = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_obj.login(emailId, pwd)
        smtp_obj.sendmail(msg['From'], [msg['To']], msg.as_string())
        smtp_obj.quit()
