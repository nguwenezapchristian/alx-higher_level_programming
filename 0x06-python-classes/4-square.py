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

    @property
    def size(self):
        """ a methode that retrieve the size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """ a methode that access the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ a methode that return the square of the object
        """
        return (self.__size**2)
