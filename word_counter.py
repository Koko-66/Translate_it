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
    Wrapper functiont that splits text string into individual words
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
    return f'\n\nWord count: {len(text)}\n'
