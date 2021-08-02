import gspread
from google.oauth2.service_account import Credentials

"""
Settings from setting up Google sheet are taken from Code Institute walk
through project "Love Sandwiches"
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Linguists_database')

linguists = SHEET.worksheet('Linguists')
data_lists = SHEET.worksheet('Data_lists')
client_data = SHEET.worksheet('Client_data')


def print_welcome():
    welcome = """Welcome to Translate it! - a quick and easy way
to find a lingusit and have your text translated.
To start, select the language from the list below
by choosing the corresponding number and then simply
follow the instructions on the screen.
"""
    print(welcome)


def main():
    print_welcome()


main()
