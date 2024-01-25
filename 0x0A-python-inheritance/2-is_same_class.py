#!/usr/bin/python3
"""
check if an instance is same as a class
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of
    the specified class; otherwise False

    Args:
        obj: an object to test
        a_class: class instance type
    """
    return type(obj) is a_class
