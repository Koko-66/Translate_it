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
languages = SHEET.worksheet('Languages')
client_data = SHEET.worksheet('Client_data')
rating = SHEET.worksheet('Rating')


def print_welcome():
    welcome = """\nWelcome to Translate it! - a quick and easy way
to find a lingusit and have your text translated.
To start, select the language from the list below
by choosing the corresponding number and then simply
follow the instructions on the screen.
"""
    print(welcome)


def print_language_list():
    language_list = languages.get_all_values()
    lang_range = len(language_list)

    i = 1
    for language in language_list:
        while i < lang_range:
            print(f'{i} - {language_list[i][0]} ({language_list[i][1]})')
            i += 1
    print('\n')


def main():
    print_welcome()
    print_language_list()


main()
