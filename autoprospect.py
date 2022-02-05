import os
import smtplib
from email.message import EmailMessage
from sheets import get_mails

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

adresses = get_mails()[1:]

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for adresse in adresses:
        msg = EmailMessage()
        msg['Subject'] = 'Message très important'
        msg['From'] =  EMAIL_ADDRESS
        msg['To'] = adresse
        msg.set_content('Bonjour Messieurs Fidèles, le nom de mon père.....')

        smtp.send_message(msg)
