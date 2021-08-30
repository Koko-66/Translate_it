from datetime import date


class Order:
    """
    Creates order class.
    """
    # Adding numbers dynamically taken from:
    # https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class

    def __init__(self, number, total_value, turnaround_time):
        self.number = number
        self.date = date.today()
        self.total_value = total_value
        self.turnaround_time = turnaround_time

    def __str__(self):
        """
        Returns order class instance as string
        """
        return '\n'.join(("\nThank you. Order details:",
                          f"{'-'*35}",
                          f"Order number: {self.number}",
                          f"Order date: {self.date}",
                          f"Order total: ${self.total_value}",
                          f"{'-'*35}"))
