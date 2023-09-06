#!/usr/bin/python3
"""
    Rectangle class

"""


class Rectangle:
    """
    a class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            i = 0
            while i < self.__height:
                a = 0
                while a < self.__width:
                    rectangle += "#"
                    a += 1
                i += 1
                if i < self.__height:
                    rectangle += "\n"
            return rectangle

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
