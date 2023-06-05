#!/usr/bin/python3

""" this is a class Rectangle that defines a rectangle """


class Rectangle:
    """ empty class rectangle """
    def __init__(self, width=0, height=0):
        """initiate the class rectangle

        Args:
            width (int): the width of a rectangle
            height (int): the height of a rectangle
        

        """
        self.__width = width
        self.__height = height
    def width(self):
        """ method to retrieve the width

        Returns:
            width of the rectangle


        """
        
        return self.__width
    @width.setter
    def width(self, value):
        """ method to st the value for the width

        Args:
            value (int): the new width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0

        
        """
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """ method to retrieve the height

        Returns:
            height of the rectangle


        """
        
        return self.__height
    @height.setter
    def height(self, value):
        """ method to set the value for height attr

        Args:
            value (int): the new height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0


        """
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
