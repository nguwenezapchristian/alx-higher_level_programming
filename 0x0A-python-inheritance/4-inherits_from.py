#!/usr/bin/python3
"""
returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    returns True or False

    Args:
        obj: object to check
        a_class: specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
