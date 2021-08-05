"""
Takes in users input and calculates word count
"""


print("\nCopy and paste your file here (Cmd+V on Linux/Mac\
    \nor Ctrl+V on Windows). You can paste in multiple texts.\
    \nOnce you're finished, press Enter and confirm upload with\
    \nCtrl+d on Linux/Mac or Crtl+z on Windows.")


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


get_user_input()
