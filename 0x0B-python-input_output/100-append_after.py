#!/usr/bin/python3

"""

    a function that inserts a line of text to a file,
    after each line containing a specific string 

"""


def append_after(filename="", search_strings="", new_string=""):
    """ defining a function that insert a line
    after a spefic string

    Arg:
        filename: the name of the text file
        search_strings: a string to insert after it
        new_string: a string to insert
    """
    with open(filename, mode='r+', encoding="utf-8") as f:
        content = f.readlines()
        all_lines = []
        f.seek(0)
        for line in content:
            all_lines.append(line)
            if search_strings in line:
                all_lines.append(new_string)
        f.writelines(all_lines)
        f.truncate()
