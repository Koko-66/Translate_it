from datetime import date
import itertools


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
                          #   f"Order number: {self.number}",
                          f"Order date: {self.date}",
                          f"Order total: ${self.total_value}",
                          f"{'-'*35}",
                          "Payment details:",
                          "Please make a payment via PayPal to",
                          "payments@translateit.com\n",
                          "Translation should be ready around",
                          f"{self.turnaround_time} after we confirm "
                          "your order."))
