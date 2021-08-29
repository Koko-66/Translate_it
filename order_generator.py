import itertools
from datetime import date
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

    def __init__(self, total_value, delivery_date):
        self.number = next(self.number_iter)
        self.date = date.today()
        self.total_value = total_value
        self.delivery_date = delivery_date
