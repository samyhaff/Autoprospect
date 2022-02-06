import gspread
from oauth2client.service_account import  ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

def get_mails(nom_sheet, colonne):
    sheet = client.open(nom_sheet).sheet1
    adresses = sheet.col_values(colonne)
    return adresses
