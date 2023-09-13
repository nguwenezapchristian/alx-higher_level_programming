#!/usr/bin/python3
def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout

    Arg:
        filename: the name of the text file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
