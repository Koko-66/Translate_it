"""
Select and sort linguist listings.

Functions:

    select_sort_criteria() -> str
    sort_by_criterion(list, str) -> list of objects (sorted)
    print_linguists(list, int) -> None
    print_sorted_linguists(list, int, str) -> None
    select_linguist(list) -> str


Variables:
    word_count
    listings
    criterion
"""
import operator


def select_sort_criteria():
    """
    Select criteria for sorting.

    If KeyError is raised asks for input again. If '0' selected, sets
    selected_crtierium to '0' and breaks the loop.
    """
    criteria = {'1': 'price', '2': 'turnaround',
                '3': 'experience', '4': 'rating'}
    print("You can sort the listed linguists by:\n")
    for criterion in criteria:
        print(f"{criterion} - {criteria[criterion]}")
    print("\nTo choose sorting criteria, type their number.")
    print("Type 0 to move on without sorting.\n")
    while True:
        try:
            criterion_selection = input(
                'Choose number from 0 to 4: \n')
            if criterion_selection != '0':
                selected_criterion = criteria[criterion_selection]
                print(f'\nLinguists sorted by: {selected_criterion.upper()}\n')
                break
            else:
                selected_criterion = '0'
                break
        except KeyError:
            print('\nInvalid selection.\
             \nPlease enter a number from 0 to 4\n')
    return selected_criterion


def sort_by_criterion(listings, criterion):
    """Sort the list of objects passed as listings by selected criterion."""
    if criterion != '0':
        if criterion == 'price':
            # Code taken from:
            # https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333
            listings = listings.sort(key=operator.attrgetter(criterion))
        else:
            listings = listings.sort(key=operator.attrgetter(criterion),
                                     reverse=True)
        return listings
    else:
        pass


def print_linguists(listings, word_count):
    """Print string representation of the linguists from the passed list."""
    for value in listings:
        print(f'\n{listings.index(value)+1} - {value.__str__(word_count)}')


def print_sorted_linguists(listings, word_count, criterion):
    """
    Print lingusits from passed list after sorting.

    Checks for sorting criteria and prints only if selection is not 0 ('none').
    """
    if criterion != '0':
        print_linguists(listings, word_count)


def select_linguist(listings):
    """
    Select linguist from the the list.

    If IndexError or ValueError is raised, asks for correct input again.
    """
    counter = len(listings)
    while True:
        try:
            linguist_selection = int(input(
                "\nTo choose the linguist select their number.\n"))
            selected_linguist = listings[linguist_selection-1]
            return selected_linguist
        except (IndexError, ValueError):
            print(f'\nInvalid selection.\
            \nPlease enter a number from 1 to {counter}\n')
