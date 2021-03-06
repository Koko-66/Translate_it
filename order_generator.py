"""
Handle order confirmation and generation. Create instances of
Order and Customer class.

Functions:
~~~~~~~~~
    confirm_order(list, int) -> None
    create_order(int, obj, int) -> obj (instance of Order)
    get_customer_data() -> obj (instance of Customer)
    push_order_to_database(int, str, str, int, obj) -> None
    create_order_confrimation_message(obj, int, str, int, obj) -> str

Variables:
~~~~~~~~~
    listings (list with linguists)
    word_count
    number
    linguist (instnce of Linguist class)
    order (instance of Order class)
    customer (instance of Customer class)
    worksheet
    language
"""

from classes.customer import Customer
from classes.order import Order
import linguist_selector
import re


def confirm_order(listings, word_count):
    """
    Ask the user to confirm order, checking for valid input ('y' or 'n').
    - If yes, break loop and move to next function.
    - If no, go back to selection of lingusist or exit the program.
    """
    order_confirmed = ""
    selection = ""
    while order_confirmed.lower() != 'y':
        order_confirmed = input("Confirm order? Y/N\n").lower()
        if order_confirmed.lower() == 'n':
            options = {"1": "Go back to linguist selection",
                       "2": "Exit program\n"}
            print("\nOrder cancelled. What do you want to do?\n")
            while True:
                selection = input(
                    f"1 - {options.get('1')} or 2 - {options.get('2')}\n")
                if selection == "1":
                    criterion = linguist_selector.select_sort_criteria()
                    linguist_selector.sort_by_criterion(listings, criterion)
                    linguist_selector.print_sorted_linguists(
                        listings, word_count, criterion)
                    selected_linguist = linguist_selector.select_linguist(
                        listings)
                    print(selected_linguist.generate_quote(word_count))
                    break
                elif selection == "2":
                    print('Exiting program...')
                    quit()
                else:
                    print("Invalid selection. Type 1 or 2.\n")
        elif order_confirmed.lower() == 'y' or order_confirmed.lower() == 'n':
            print("\nOrder placed.")
            break
        else:
            print("Invalid input. Type in 'Y' or 'N'.\n")


def create_order(number, linguist, word_count):
    """Create an instance of Order."""
    total_value = linguist.calculate_total_price(word_count)
    turnaround_time = linguist.calculate_turnaround_time(word_count)
    order = Order(number, total_value, turnaround_time)
    print(str(order))
    return order


def get_customer_data():
    """Get name and email from customer; validate e-mail's format."""
    print("\nPlease provide your details.")
    name = input("\nYour name: \n")
    # regex and code in the if statement taken from:
    # https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    while True:
        email = input("\nYour e-mail address: \n")
        if re.fullmatch(regex, email):
            print("\nThank you! You will receive the \
confirmation email shortly.\nIf you don't receive the \
e-mail contact support team at:\
\ntranslateit7@gmail.com.")
            break
        else:
            print("\nInvalid e-mail, try again.\n")
    customer = Customer(name, email)
    return customer


def push_order_to_database(order, worksheet, language, word_count, customer):
    """Push order data back to the database."""
    data = [order.number, str(order.date), language, word_count,
            order.total_value, customer.name, customer.email]
    worksheet.append_row(data)


def create_order_confrimation_message(customer, order, language,
                                      word_count, linguist):
    """Create message with order details to send to customer via email."""
    turnaround_time = linguist.calculate_turnaround_time(word_count)
    message = "\n".join((f"Hello {customer.name},\n",
                         "Thank you for your order! "
                         "Here are your order details:",
                         f"{'-'*35}",
                         f"<strong>Order number</strong>: {order.number}",
                         f"<strong>Order date</strong>: {order.date}",
                         f"<strong>Language</strong>: {language}",
                         f"<strong>Word count</strong>: {word_count}",
                         f"<strong>Linguist</strong>: {linguist.name}",
                         "<strong>Order total</strong>: "
                         f"${order.total_value}\n",
                         f"{'-'*35}",
                         "<strong>Payment details</strong>:",
                         "Please make a payment via PayPal to",
                         "payments@translateit.com\n",
                         "Translation should be ready in around "
                         f"<strong>{turnaround_time}</strong> "
                         "after we confirm your order."))
    return message
