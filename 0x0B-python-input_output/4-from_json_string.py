#!/usr/bin/python3

"""

    a function that returns an object (Python data structure)
    represented by a JSON string

"""


import json


def from_json_string(my_obj):
    """ a function that returns an object

    Arg:
        my_obj: the object(string)
    """
    return json.loads(my_obj)
