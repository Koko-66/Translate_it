
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
        return f"""ID {self.no}: {self.name} - {self.language};
            Experience: {self.experience} years;
            Price: {self.price}/word;
            Words/Day: {self.turnaround};
            Rating: {self.rating}"""

