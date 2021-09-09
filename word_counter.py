"""
Calculate word count for text input by the user.

Funtions:
~~~~~~~~
    print_instructions() -> None
    split_text(func) -> list
    get_user_input -> str
    return_word_count(list) -> int
    run_word_count -> int

Variables:
~~~~~~~~~
    text
"""
import re


def print_instructions():
    """Print instructions for the user on how to copy text."""
    instructions = """Copy and paste your file here (Cmd+V on Linux/Mac
or Ctrl+V on Windows). You can paste in multiple lines of text.
Once you're finished, hit Enter and confirm upload with
Ctrl+d on Linux/Mac or Crtl+z on Windows.\n"""
    print(instructions)


def split_text(func):
    """
    Wrapper function. Split the text string returned by the function passed
    as the argument into individual words to prepare it for counting.
    """
    text = func()
    text = re.split(r'\s|\n|/', text)
    text = ' '.join(text).split()  # trims off spaces and empty strings
    return text


def get_user_input():
    """Return multiline input from the user as one string."""
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
    """
    Return word count.

    Takes in text converted into a list of words that is passed as an argument
    and returns the length of the list as word count.
    """
    print("\n\nCounting...")
    word_count = len(text)
    print(f"\n\nWord count: {word_count}\n")
    return word_count


def run_word_count():
    """
    Run all functions to get the user's input and calculate word count.

    Checks if word count is '0' and requests text input again if yes.
    """
    print_instructions()
    while True:
        text = split_text(get_user_input)
        word_count = return_word_count(text)
        if word_count == 0:
            print("\nWord count cannot be 0.")
            print("Please provide text to translate.")
        else:
            return word_count
