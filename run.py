import gspread
from google.oauth2.service_account import Credentials
import word_counter
import linguist_selector
import order_generator
from classes.linguist import Linguist
import send_confirmation


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
order_data = SHEET.worksheet('Order_data')
rating = SHEET.worksheet('Rating')


def print_welcome():
    """
    Prints welcome message with intro to the program.
    """
    welcome = """\nWelcome to Translate it! - a quick and easy way
to find a lingusit and have your text translated.
To start, select the language from the list below
by choosing the corresponding number and then simply
follow the instructions on the screen.\n"""
    print(welcome)


def create_lang_dict():
    """
    Creates dictionary with index as key and language with locale as value.
    """
    language_list = languages.get_all_values()
    lang_dict = {}
    for i in range(1, len(language_list)):
        language = language_list[i][0]
        lang_dict.update({f'{i}': language})
        i += 1
    return lang_dict


def print_languages():
    """
    Prints list of languages for selection.
    """
    lang_dict = create_lang_dict()
    for key, value in lang_dict.items():
        print(f'{key} - {value}')


def confirm_selection(func):
    """
    Ask user to confirm their selection and reruns the function passed.
    """
    confirmed = ''
    while confirmed.lower() != 'y':
        confirmed = input("Confirm selection? Y/N\n").lower()
        if confirmed.lower() == 'n':
            print("\nPrevious selection cancelled. Try again.\n")
            func()
        elif confirmed.lower() == 'y':
            print("\nSelection confirmed.\n")
            break
        else:
            print("Invalid entry. Please type 'Y' or 'N'.")


def language_selector():
    """
    Get language selection from the user and return for later use.
    """
    lang_dict = create_lang_dict()
    lang_count = len(languages.col_values(1))-1

    while True:
        try:
            lang_selection = input(
                f'\nChoose number from 1 to {lang_count}: ')
            selected_lang = lang_dict[lang_selection]
            print(f'\nYour selection: {selected_lang}\n')
            break
        except KeyError:
            print(f'\nInvalid selection.\
            \nPlease enter a number from 1 to {lang_count}\n')
    return selected_lang


def return_linguists(language):
    """
    Return a list of row numbers containing selected language.
    """
    cells = linguists.findall(language)
    rows = []
    for cell in cells:
        rows.append(cell.row)
    listings = []
    for row in rows:
        listing = linguists.row_values(row)
        linguist = Linguist(
            listing[0], f'{listing[1]} {listing[2]}',
            listing[3], int(listing[4]), listing[5],
            listing[6], listing[7])
        listings.append(linguist)
    return listings


def generate_order_number():
    """
    Generate order number based on the last entry in the order worksheet of the
    database. If none present, sets order number to 101.
    """
    try:
        order_number = int(order_data.col_values(1)[-1]) + 1
    except ValueError:
        pass
        order_number = 101
    return order_number


def main():
    """
    Run program functions
    """
    print_welcome()
    create_lang_dict()
    print_languages()
    selected_lang = language_selector()
    confirm_selection(language_selector)
    word_count = word_counter.run_word_count()
    listings = return_linguists(selected_lang)
    linguist_selector.print_linguists(listings, word_count)
    criterium = linguist_selector.select_sort_criteria()
    linguist_selector.sort_by_criterium(listings, criterium)
    linguist_selector.return_sorted_linguists(listings, word_count, criterium)
    selected_linguist = linguist_selector.select_linguist(listings)
    print(selected_linguist.generate_quote(word_count))
    order_generator.confirm_order(listings, word_count)
    order_number = generate_order_number()
    order = order_generator.create_order(
        order_number, selected_linguist, word_count)
    customer = order_generator.get_customer_data()
    order_generator.push_order_to_database(
        order, order_data, selected_lang, word_count, customer)
    message = order_generator.create_order_confrimation_message(
        customer, order, selected_lang, word_count, selected_linguist)
    send_confirmation.send_email_confimation(
        order.number, customer.email, message)


main()
