#!/usr/bin/python3

"""Define a class square"""


class Square:
    """ class that defines a square by it's size
    """
    def __init__(self, size=0):
        """ a methode to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ a methode that return the square of the object
        """
        return (self.__size**2)
