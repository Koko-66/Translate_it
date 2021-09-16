"""Create Order class."""
from datetime import date


class Order:
    """
    A class to represent order.

    Attrubutes:
    ~~~~~~~~~~
    number: int (order number, generated in the run.py module)
    date: datetime (order date)
    total_value: float (the total value of the order - price)
    turnaround_time: str (turnaround time representation as string
            returned by the Linguist calculate_turnaround_time method
            in the order_generator)
    """
    # Adding numbers dynamically taken from:
    # https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class

    def __init__(self, number, total_value, turnaround_time):
        """Construct the order object."""
        self.number = number
        self.date = date.today()
        self.total_value = total_value
        self.turnaround_time = turnaround_time

    def __str__(self):
        """Return order class instance as string."""
        return '\n'.join(("\nThank you. Order details:",
                          f"{'-'*35}",
                          f"Order number: {self.number}",
                          f"Order date: {self.date}",
                          f"Order total: ${self.total_value}",
                          f"{'-'*35}"))
