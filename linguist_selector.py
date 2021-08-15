
"""
Create Linguist class.
Print linguist list according to selection criteria.
"""


class Linguist:
    """
    Creates linguist class
    """
    def __init__(self, no, name, language,
                 experience, price, turnaround, rating):
        self.no = no
        self.name = name
        self.language = language
        self.experience = experience
        self.price = price
        self.turnaround = turnaround
        self.rating = rating

    def __str__(self):
        """
        Returns class instance as string
        """
        return ' |$| '.join((f"ID {self.no}: {self.name} - {self.language}",
                             f"Experience: {self.experience} years",
                             f"Price: {self.price}/word",
                             f"Words/Day: {self.turnaround}",
                             f"Rating: {self.rating}",))

