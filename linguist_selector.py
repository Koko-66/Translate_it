import math
"""
Create Linguist class.
Print linguist list according to selection criteria.
"""

WORKING_HOURS_DAY = 6


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

    def calculate_total_price(self, word_count):
        """
        Calculate total price per linguist.
        """
        total_price = round(word_count * self.price, 2)
        return f"Total price: ${total_price}"

    def calculate_turnaround_time(self, word_count):
        """
        Calculate time needed to translate the text
        """
        words_per_hour = round(self.turnaround/WORKING_HOURS_DAY)
        turnaround_hours = round(word_count/words_per_hour)
        if turnaround_hours < 6:
            if turnaround_hours == 1 or word_count < words_per_hour:
                return "Turnaround time: ca 1 hour."
            else:
                return f"Turnaround time: ca {turnaround_hours} hours."
        else:
            turnaround_days = turnaround_hours/6
            full_days = math.trunc(turnaround_days)
            turnaround_hours = round((turnaround_days - full_days) * 6)
            if turnaround_days == 1:
                return "Turnaround time: ca 1 day."
            else:
                if turnaround_hours == 0:
                    return f"Turnaround time: ca {turnaround_days} day(s)."
                else:
                    return f"Turnaround time: ca \
{full_days} days and {turnaround_hours} hours."


koko = Linguist(2, 'koko', 'Polish', 3, 0.06, 1300, 2)

pricing = koko.calculate_total_price(834)
print(pricing)
turnaround = koko.calculate_turnaround_time(1516)
print(turnaround)
