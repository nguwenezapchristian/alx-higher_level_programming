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
        self.width = width
        self.height = height
    @property
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
    def area(self):
        """ method calculate an area

        Returns:
            the area of a rectangle


        """
        return self.__height * self.__width
    def perimeter(self):
        """ method to calculate the perimeter

        Returns:
            the perimeter of a rectangle


        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
    def __str__(self):
        """ return string # as a rectangle

        Returns:
            string of the rectangle


        """
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        else:
            for i in range(self.__height):
                rectangle += ("#" * self.__width) + "\n"
            return rectangle[:-1]
    def __repr__(self):
        """ return a string representation of the rectangle

        Returns:
            string representation

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
