#!/usr/bin/python3
"""

    a class Student that defines a student


"""


class Student():
    """ a class Student that defines a student """
    def __init__(self, first_name, last_name, age):
        """ constructor of a student

        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ class to json

        Args:
            attrs: list of attribute
        """
        if attrs is None:
            return {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                }
        else:
            dictionary = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dictionary[attr] = getattr(self, attr)
            return dictionary
