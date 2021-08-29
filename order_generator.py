import itertools
from datetime import date
import linguist_selector
"""
Create customer and order class.
Print order and send details to the customer
"""

class Customer:
    """
    Creates customer class.
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    """
    Creates order class.
    """
    # Adding numbers dynamically taken from:
    # https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class
    number_iter = itertools.count()

    def __init__(self, total_value, turnaround_time):
        instances = []
        self.number = next(self.number_iter)
        self.date = date.today()
        self.total_value = total_value
        self.turnaround_time = turnaround_time
        instances.append(self)

    def __str__(self):
        """
        Returns order class instance as string
        """
        return '\n'.join(("\nThank you for your oder! Your order details.",
                          f"{'-'*35}",
                          f"Order number: {self.number}",
                          f"Order date: {self.date}",
                          f"Order total: ${self.total_value}",
                          f"{'-'*35}",
                          "Payment details:",
                          "Please make a payment via PayPal to",
                          "payments@translateit.com\n",
                          "Translation should be ready around",
                          f"{self.turnaround_time} after we confirm \
your order."))


def create_order(Linguist, word_count):
    """
    Creates order instance
    """
    total_value = linguist_selector.Linguist.calculate_total_price(
        Linguist, word_count)
    turnaround_time = Linguist.calculate_turnaround_time(word_count)
    order = Order(total_value, turnaround_time)
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


def push_order_to_database(Order, worksheet, language, word_count, Customer):
    data = [Order.number, str(Order.date), language, word_count,
            Order.total_value, Customer.name, Customer.email]
    worksheet.append_row(data)
