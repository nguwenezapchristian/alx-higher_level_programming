#!/usr/bin/python3

"""

     a function that writes an Object to
     a text file, using a JSON representation

"""


import json


def save_to_json_file(my_obj, filename):
    """  a function that writes an Object to
    a text file, using a JSON representation

    Arg:
        my_obj: the object(string)
        filename: json file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        to_json = json.dumps(my_obj)
        f.write(to_json)
