#!/usr/bin/python3

"""

     a function that creates an Object from a “JSON file”

"""


import json


def load_from_json_file(filename):
    """  a function that creates an
    Object from a “JSON file”

    Arg:
        filename: json file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        content = f.read()
        return json.loads(content)
