import math
import operator

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

    def calculate_turnaround_time(self, word_count):
        """
        Calculate time needed to translate the text.
        Minimum turnaround time is one hour.
        """
        words_per_hour = round(float(self.turnaround)/WORKING_HOURS_DAY)
        turnaround_hours = round(word_count/words_per_hour)
        if turnaround_hours < 6:
            if turnaround_hours == 1 or word_count < words_per_hour:
                return "1 hour."
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
                    return f"{turnaround_days} day(s)."
                else:
                    return f"{full_days} days and {turnaround_hours} hours."

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


def sort_by_criterium(listings, criterium):
    """
    Sort the list of objects returned earlier by selected criterium.
    """
    if criterium != '0':
        # Code taken from:
        # https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333
        listings = listings.sort(key=operator.attrgetter(criterium))
        return listings
    else:
        pass


def select_sort_criteria():
    """
    Select criteria for sorting
    """
    criteria = {'1': 'price', '2': 'turnaround',
                '3': 'experience', '4': 'rating'}
    print("You can sort the listed linguists by:\n")
    for criterium in criteria:
        print(f"{criterium} - {criteria[criterium]}")
    print("\nTo choose sorting criteria, type their number.")
    print("Select 0 to print without sorting.\n")
    while True:
        try:
            criterium_selection = input(
                'Choose number from 0 to 4: \n')
            if criterium_selection != '0':
                selected_criterium = criteria[criterium_selection]
                print(f'Linguists sorted by: {selected_criterium.upper()}\n')
                break
            else:
                selected_criterium = '0'
                break
        except KeyError:
            print('\nInvalid selection.\
             \nPlease enter a number from 0 to 4\n')
    return selected_criterium


def print_linguists(listings, word_count):
    """
    Print linguists matching the language selected by the user.
    """
    for value in listings:
        print(f'{listings.index(value)+1} - {value.__str__(word_count)}')


def select_linguist(listings):
    """
    Select linguist from the listed options
    """
    counter = len(listings)
    while True:
        try:
            linguist_selection = int(input(
                "\nTo choose the linguist select their number.\n"))
            selected_linguist = listings[linguist_selection-1]
            # print(f'\nYour selection: {selected_linguist.name}\n')
            return selected_linguist
        except (IndexError, ValueError):
            print(f'\nInvalid selection.\
            \nPlease enter a number from 1 to {counter}\n')
