"""
Create customer and order class.
Print order and send details to the customer
"""

from classes.customer import Customer
from classes.order import Order
import linguist_selector


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
                    f"1 - {options.get('1')} or 2 - {options.get('2')}")
                if selection == "1":
                    linguist_selector.print_linguists(listings, word_count)
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
            print("Order confirmed")
            break
        else:
            print("Invalid input. Type in 'Y' or 'N'.\n")


def create_order(number, linguist, word_count):
    """
    Creates order instance
    """
    total_value = linguist.calculate_total_price(word_count)
    turnaround_time = linguist.calculate_turnaround_time(word_count)
    order = Order(number, total_value, turnaround_time)
    print(str(order))
    return order


def get_customer_data():
    """
    Get customer name and email.
    """
    print("Please provide your details.")
    name = input("\nYour name: ")
    email = input("\nYour e-mail address: ")
    customer = Customer(name, email)
    return customer


def push_order_to_database(order, worksheet, language, word_count, customer):
    """
    Push order data back to the database for record.
    """
    data = [order.number, str(order.date), language, word_count,
            order.total_value, customer.name, customer.email]
    worksheet.append_row(data)


def create_order_confrimation_message(customer, order, language,
                                      word_count, linguist):
    turnaround_time = linguist.calculate_turnaround_time(word_count)
    message = "\n".join((f"Thank you for your order, {customer.name}",
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
                         "Translation should be ready around "
                         f"<strong>{turnaround_time}</strong> "
                         "after we confirm your order."))
    return message
