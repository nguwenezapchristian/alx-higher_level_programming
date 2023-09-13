#!/usr/bin/python3

"""

    a function that appends a string at the end of
    a text file (UTF8) and returns the number of characters added

"""


def append_write(filename="", text=""):
    """ a function that appends a string at the end of
    a text file (UTF8) and returns the number of characters added
    Arg:
        filename: the name of the text file
        text: string to add to a text file
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
