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
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
