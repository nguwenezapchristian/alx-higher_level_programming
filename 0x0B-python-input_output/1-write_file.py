#!/usr/bin/python3

"""

    a function that writes a string to a text file (UTF8)
    and returns the number of characters written

"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
    returns the number of characters written

    Arg:
        filename: the name of the text file
        text: string to add to a text file
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
