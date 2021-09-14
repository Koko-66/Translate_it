"""Create Linguist class."""
import math

# Number of working hours per day
WORKING_HOURS_DAY = 6


class Linguist:
    """
    A class to represent linguist.

    Attributes:
    ~~~~~~~~~~

    no: str (linguists id)
    name: str (linguists full name)
    language: str (linguist's working language)
    experinece: int (years of experience)
    price: float (linguist's pricing)
    turnaround: int (how many words the lingusits can translate)
    rating: int (linguist's rating)

    Methods:
    ~~~~~~~

    calculate_total_price(float):
            Return total price for the provided text as float.
    turnaround_time_as_float(int):
            Return turnaround time for translating provided text as float
            for comparison.
    calculate_turnaround_time(int):
            Return turnaround time for translating provided text as string
            with information.
    generate_quote(int):
            Return summary of the order with selected language, linguist,
            total price and turnaround time

    Variables:
        word_count
    """

    def __init__(self, no, name, language,
                 experience, price, turnaround, rating):
        """Construct the linguist object."""
        self.no = no
        self.name = name
        self.language = language
        self.experience = experience
        self.price = price
        self.turnaround = turnaround
        self.rating = rating

    def __str__(self, word_count):
        """
        Return linguist listing as string.

        Takes word_count as parameter to calculates total_price and
        turnaround time.
        """
        total_price = "{:.2f}".format(self.calculate_total_price(word_count))
        turnaround_time = self.calculate_turnaround_time(word_count)
        return ' ** '.join((f"ID {self.no}: {self.name} - {self.language}",
                            f"\n{' '*7}Experience: {self.experience} years",
                            f"Rating: {self.rating}",
                            f"\n\n{' '*7}Price/word: {self.price}",
                            f"Total: ${total_price}",
                            f"\n{' '*7}Turnaround time: ca {turnaround_time}",
                            f"\n{'_'*50}\n"))

    def calculate_total_price(self, word_count):
        """Return total price for the word count."""

        total_price = round(word_count * float(self.price), 2)
        return total_price

    def turnaround_time_as_float(self, word_count):
        """
        Calculate and return time needed to translate the text and return it
        as a float.

        Takes word count as argument. Minimum turnaround time: one hour.
        """
        words_per_hour = round(float(self.turnaround)/WORKING_HOURS_DAY)
        turnaround_hours = round(word_count/words_per_hour)
        if word_count < words_per_hour:
            return 1
        else:
            return turnaround_hours

    def calculate_turnaround_time(self, word_count):
        """
        Calculate and return time needed to translate the text and return
        printable information.

        Takes word count as argument. Minimum turnaround time: one hour.
        """
        turnaround_hours = self.turnaround_time_as_float(word_count)
        if turnaround_hours < WORKING_HOURS_DAY:
            if turnaround_hours == 1:
                return "1 hour"
            else:
                return f"{turnaround_hours} hours"
        else:
            turnaround_days = turnaround_hours/WORKING_HOURS_DAY
            full_days = math.trunc(turnaround_days)
            turnaround_hours = round((turnaround_days - full_days)
                                     * WORKING_HOURS_DAY)
            if turnaround_days == 1:
                return "1 day"
            else:
                if turnaround_hours == 0:
                    if full_days == 1:
                        return f"{math.trunc(turnaround_days)} day"
                    else:
                        return f"{math.trunc(turnaround_days)} days"
                else:
                    if full_days == 1:
                        return f"{full_days} day and {turnaround_hours} hours"
                    else:
                        return f"{full_days} days and {turnaround_hours} hours"

    def generate_quote(self, word_count):
        """Print quotation details for selected linguist."""

        total_price = self.calculate_total_price(word_count)
        turnaround_time = self.calculate_turnaround_time(word_count)
        return '\n'.join(("\nYour quote: ",
                          f"{'-'*40}",
                          f"Translator: {self.name}",
                          f"Language: {self.language}",
                          f"Total price: ${total_price}",
                          f"Turnaround time: ca {turnaround_time}\n"))
