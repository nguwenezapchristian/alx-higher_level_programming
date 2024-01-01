#!/usr/bin/python3
"""
check if the object is an instance of, or an
instance of a class that inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    returns True or False

    Args:
        obj: object to check
        a_class: specified class
    """
    return isinstance(obj, a_class)
