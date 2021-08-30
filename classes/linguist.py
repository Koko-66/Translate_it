import math

# Number of working hours per day
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

    def __str__(self, word_count):
        """
        Returns linguist listing as string
        """
        total_price = self.calculate_total_price(word_count)
        turnaround_time = self.calculate_turnaround_time(word_count)
        return ' ** '.join((f"ID {self.no}: {self.name} - {self.language}",
                            f"\n{' '*7}Experience: {self.experience} years",
                            f"Rating: {self.rating}",
                            f"\n\n{' '*7}Price/word: {self.price}",
                            f"Total: ${total_price}",
                            # f"Words/Day: {self.turnaround}"
                            # f"Word count: {word_count}",
                            f"\n{' '*7}Turnaround time: ca {turnaround_time}",
                            f"\n{'_'*50}\n"))

    def calculate_total_price(self, word_count):
        """
        Calculate total price per linguist.
        """
        total_price = round(word_count * float(self.price), 3)
        return total_price

    def turnaround_time_as_float(self, word_count):
        """
        Calculate time needed to translate the text and return it as a float.
        Minimum turnaround time is one hour.
        """
        words_per_hour = round(float(self.turnaround)/WORKING_HOURS_DAY)
        turnaround_hours = round(word_count/words_per_hour)
        if word_count < words_per_hour:
            return 1
        else:
            return turnaround_hours

    def calculate_turnaround_time(self, word_count):
        """
        Calculate time needed to translate the text.
        Minimum turnaround time is one hour.
        """
        turnaround_hours = self.turnaround_time_as_float(word_count)
        # words_per_hour = round(float(self.turnaround)/WORKING_HOURS_DAY)
        # turnaround_hours = round(word_count/words_per_hour)
        if turnaround_hours < 6:
            if turnaround_hours == 1:
                return "1 hour"
            else:
                return f"{turnaround_hours} hours."
        else:
            turnaround_days = turnaround_hours/6
            full_days = math.trunc(turnaround_days)
            turnaround_hours = round((turnaround_days - full_days) * 6)
            if turnaround_days == 1:
                return "1 day."
            else:
                if turnaround_hours == 0:
                    return f"{turnaround_days} day(s)"
                else:
                    return f"{full_days} day(s) and {turnaround_hours} hours"

    def generate_quote(self, word_count):
        """
        Print quotation details for selected linguist
        """
        total_price = self.calculate_total_price(word_count)
        turnaround_time = self.calculate_turnaround_time(word_count)
        return '\n'.join(("\nYour quote: ",
                          f"{'-'*40}",
                          f"Translator: {self.name}",
                          f"Language: {self.language}",
                          #   f"Word count: {word_count}",
                          f"Total price: ${total_price}",
                          f"Turnaround time: ca {turnaround_time}\n"))
