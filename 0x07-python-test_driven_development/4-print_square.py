#!/usr/bin/python3
def print_square(size):
    """ function that prints a square with the character #
    Arg:
        size(int): size of a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size > 100:
        raise OverflowError("too large value for a size of a square")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print(" ")
    else:
        i = 0
        while i < size:
            b = 0
            while b < size:
                print("#", end="")
                b += 1
            print()
            i += 1
