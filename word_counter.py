"""
Takes in users input and calculates word count
"""


print("\nCopy and paste your file here (Cmd+V on Linux/Mac\
    \nor Ctrl+V on Windows). You can paste in multiple texts.\
    \nOnce you're finished, confirm upload with\
    \nCtrl+d on Linux/Mac or Crtl+z on Windows.\n")


def split_text(func):
    """
    Wrapper functiont that splits text string into individual words
    to prepare for counting.
    """
    text = func()
    text = text.split(' ')
    return text


@split_text
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


text = get_user_input
print(text)
print(len(text))
