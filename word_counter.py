import re
"""
Takes in users input and calculates word count
"""


def print_instructions():
    """
    Print instructions for the user on how to copy text
    """
    instructions = "Copy and paste your file here (Cmd+V on Linux/Mac\
        \nor Ctrl+V on Windows). You can paste in multiple texts.\
        \nOnce you're finished, confirm upload with\
        \nCtrl+d on Linux/Mac or Crtl+z on Windows.\n"
    print(instructions)


def split_text(func):
    """
    Wrapper function that splits text string into individual words
    to prepare for counting.
    """
    text = func()
    text = re.split(r'\s|\n|/', text)
    text = ' '.join(text).split()  # trims off spaces and empty strings
    return text


def get_user_input():
    """
    Gets multiline input from the user and converts it to one string
    """
    # Code below taken from:
    # https://stackoverflow.com/questions/34889012/how-to-paste-multiple-lines-of-text-into-python-input
    text = []
    try:
        while True:
            text.append(input())
    except EOFError:
        pass
    text = "\n".join(text)
    return text


def return_word_count(text):
    print("Counting...")
    word_count = len(text)
    print(f"\n\nWord count: {word_count}\n")
    return word_count


def run_word_count():
    print_instructions()
    while True:
        text = split_text(get_user_input)
        word_count = return_word_count(text)
        if word_count == 0:
            print("Word count cannot be 0.")
            print("Please provide text to translate.")
        else:
            return word_count


# run_word_count()
