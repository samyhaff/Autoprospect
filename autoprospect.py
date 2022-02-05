import os
import smtplib
from email.message import EmailMessage
from sheets import get_mails

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Test subject'
msg['From'] =  EMAIL_ADDRESS
msg['To'] = 'haffoudhisamy@gmail.com'
msg.set_content('test content')

adresses = get_mails()
print(adresses)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
