#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of
    the specified class; otherwise False

    Args:
        obj: an object to test
        a_class: class instance type
    """
    if a_class != object:
        if isinstance(obj, a_class):
            return True
        else:
            return False
