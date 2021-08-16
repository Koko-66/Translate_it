
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

    # def to calculate price for file
    def calculate_total_price(self, word_count):
        """
        Calculate total price per linguist.
        """
        total_price = word_count * self.price
        return total_price

    # def to calculate turnaround time
    


koko = Linguist(2, 'koko', 'Polish', 3, 0.06, 300, 2)

pricing = round(koko.calculate_total_price(234), 2)
print(pricing)
