"""
Select criteria for sorting linguists and sort their listings.
Print linguist list according to selection and then sorting criteria.
"""
import operator


def sort_by_criterium(listings, criterium):
    """
    Sort the list of objects returned earlier by selected criterium.
    """
    if criterium != '0':
        if criterium == 'price':
            # Code taken from:
            # https://stackoverflow.com/questions/4010322/sort-a-list-of-class-instances-python#comment4297852_4010333
            listings = listings.sort(key=operator.attrgetter(criterium))
        else:
            listings = listings.sort(key=operator.attrgetter(criterium),
                                     reverse=True)
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
    print("Type 0 to move on without sorting.\n")
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
        print(f'\n{listings.index(value)+1} - {value.__str__(word_count)}')


def print_sorted_linguists(listings, word_count, criterium):
    """
    Prints lingusits after they've been sorted only if sorting
    criteria is selected.
    """
    if criterium != '0':
        print_linguists(listings, word_count)


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
