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
    """
    Prints welcome message with intro to the program.
    """
    welcome = """\nWelcome to Translate it! - a quick and easy way
to find a lingusit and have your text translated.
To start, select the language from the list below
by choosing the corresponding number and then simply
follow the instructions on the screen.
"""
    print(welcome)


def create_all_langs_list():
    """
    Creates a list with languages and their locales as one string.
    """
    language_list = languages.get_all_values()
    lang_range = len(language_list)
    i = 1
    all_langs_list = []
    for language in language_list:
        while i < lang_range:
            lang_with_locale = f'{language_list[i][0]} ({language_list[i][1]})'
            all_langs_list.append(f'{lang_with_locale}')
            i += 1
    return all_langs_list


def create_lang_dict():
    """
    Creates dictionary with index as key and language with locale as value.
    """
    language_list = create_all_langs_list()
    lang_dict = {}
    for i in range(0, len(language_list)):
        lang_dict.update({f'{i}': language_list[i]})
        i += 1
    return lang_dict


def print_languages():
    """
    Prints list of languages for selection.
    """
    lang_dict = create_lang_dict()
    for key, value in lang_dict.items():
        print(f'{key} - {value}')


def main():
    print_welcome()
    create_lang_dict()
    print_languages()


main()
