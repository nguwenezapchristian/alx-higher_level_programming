#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """  prints My name is <first name> <last name>

    Args:
        first_name(str): first name
        last_name(str): last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {last_name}")
