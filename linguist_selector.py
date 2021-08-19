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

    def __str__(self):
        """
        Returns class instance as string
        """
        return ' ** '.join((f"ID {self.no}: {self.name} - {self.language}",
                            f"\n{' '*7}Experience: {self.experience} years",
                            f"Rating: {self.rating}",
                            f"\n{' '*7}Price: {self.price}/word",
                            f"Words/Day: {self.turnaround}\n"
                            f"{'_'*50}\n"))

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


def sort_by_criterium(listings, criterium):
    """
    Sort the list of objects returned earlier by selected criterium.
    """
    # Code taken from:
    # https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333
    listings = listings.sort(key=operator.attrgetter(criterium))
    return listings


def select_sort_criteria():
    """
    Select criteria for sorting
    """
    criteria = {'1': 'price', '2': 'turnaround', '3': 'experience',
                '4': 'rating'}
    print("You can choose to sort the listed linguists by:\n")
    for criterium in criteria:
        print(f"{criterium} - {criteria[criterium]}")
    print("\nPlease make your selection by choosing the relevant number")
    print("If you do not wish to sort the listings, select 0.\n")
    while True:
        try:
            criterium_selection = input(
                '\nChoose number from 0 to 4: ')
            selected_criterium = criteria[criterium_selection]
            print(f'\nYour selection: {selected_criterium}\n')
            break
        except KeyError:
            print('\nInvalid selection.\
             \nPlease enter a number from 0 to 4\n')
    return selected_criterium


koko = Linguist(2, 'koko', 'Polish', 3, 0.06, 1300, 2)

# pricing = koko.calculate_total_price(834)
# print(pricing)
# turnaround = koko.calculate_turnaround_time(1516)
# print(turnaround)

# select_sort_criteria()
