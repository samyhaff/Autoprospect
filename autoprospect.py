#!/bin/python

import os
import argparse
import smtplib
from email.message import EmailMessage
from sheets import get_mails

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

parser = argparse.ArgumentParser(description='Un script pour l\'envoi automatique de mails à une BDD')
parser.add_argument("contenu", type=str, help='fichier contenant le mail à envoyer')
parser.add_argument('-o', '--objet', type=str, help='object du mail', default='')
args = parser.parse_args()

contenu = args.contenu
objet = args.objet

adresses = get_mails()[1:]

with open('contenu_mail', 'r') as fichier:
    contenu = fichier.read()

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for adresse in adresses:
        msg = EmailMessage()
        msg['Subject'] = objet
        msg['From'] =  EMAIL_ADDRESS
        msg.set_content(contenu)
        msg['To'] = adresse

        smtp.send_message(msg)
