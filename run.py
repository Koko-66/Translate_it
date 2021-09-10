"""
Compile all modules and functions and run program.
Set up link to the database and define functions relying on data from
the database.

Functions:
~~~~~~~~~
    print_welcome(str) -> None
    create_lang_dict() -> dict
    print_languages() -> None
    confirm_selection(func) -> None
    language_selector() -> str
    return_linguists(str) -> Any (list of objects)
    generate_order_number() -> int
    main()

Variables:
~~~~~~~~~
    func
    language

Variables created and used in the main() function:
~~~~~~~~~
    selected_lang
    word_count
    listings
    criterion
    selected_linguist
    order_number
    order
    customer
    message
"""
import gspread
from google.oauth2.service_account import Credentials
import word_counter
import linguist_selector
import order_generator
from classes.linguist import Linguist
import confirmation_mailer


# Settings for setting up Google sheet are taken from the
# Code Institute's walk through project "Love Sandwiches"
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

try:
    SHEET = GSPREAD_CLIENT.open('Database')
    linguists = SHEET.worksheet('Linguists')
    languages = SHEET.worksheet('Languages')
    order_data = SHEET.worksheet('Order_data')
    rating = SHEET.worksheet('Rating')
except gspread.exceptions.SpreadsheetNotFound:
    print("\nWe're sorry, an error has ocurred.")
    print("Please contact support at translateit7@gmail.com\n")
    quit()


def print_welcome():
    """Print welcome message with intro to the program."""
    welcome = """\nWelcome to Translate it! - a quick and easy way
to find a lingusit and have your text translated.
To start, select the language from the list below
by choosing the corresponding number and then
follow the instructions on the screen.\n"""
    print(welcome)


def create_lang_dict():
    """Return dictionary with all languages from the database."""
    language_list = languages.get_all_values()
    lang_dict = {}
    for i in range(1, len(language_list)):
        language = language_list[i][0]
        lang_dict.update({f'{i}': language})
        i += 1
    return lang_dict


def print_languages():
    """Print list of languages from the dictionary for selection."""
    lang_dict = create_lang_dict()
    for key, value in lang_dict.items():
        print(f'{key} - {value}')


def confirm_selection(func):
    """
    Ask user to confirm their selection and re-run the function passed
    if not confirmed.
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
    Return language selected by the user.

    Validates user input and asks to choose again until no KeyError
    is raised.
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
    Return a list of linguists with the language passed as argument.

    Iterates through the list of rows containing the selected language pulled
    from the database and creates a Linguist instance from data in each row.
    """
    cells = linguists.findall(language)
    rows = []
    for cell in cells:
        rows.append(cell.row)
    listings = []
    for row in rows:
        listing = linguists.row_values(row)
        id = listing[0]
        name = f'{listing[1]} {listing[2]}'
        language = listing[3]
        experience = int(listing[4])
        price = float(listing[5])
        turnaround = int(listing[6])
        rating = int(listing[7])
        linguist = Linguist(id, name, language, experience,
                            price, turnaround, rating)
        listings.append(linguist)
    return listings


def generate_order_number():
    """
    Generate order number based on the last entry in the order worksheet
    in the database. If none present, set order number to 101.
    """
    try:
        order_number = int(order_data.col_values(1)[-1]) + 1
    except ValueError:
        pass
        order_number = 101
    return order_number


def main():
    """
    Run program functions.

    If the user hits EOF, quits the program.
    """
    try:
        print_welcome()
        create_lang_dict()
        print_languages()
        selected_lang = language_selector()
        confirm_selection(language_selector)
        word_count = word_counter.run_word_count()
        listings = return_linguists(selected_lang)
        linguist_selector.print_linguists(listings, word_count)
        criterion = linguist_selector.select_sort_criteria()
        linguist_selector.sort_by_criterion(listings, criterion)
        linguist_selector.print_sorted_linguists(
            listings, word_count, criterion)
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
        confirmation_mailer.send_email_confimation(
            order.number, customer.email, message)
    except (EOFError, KeyboardInterrupt):
        print("\nExiting program...\n")
        quit()


main()
