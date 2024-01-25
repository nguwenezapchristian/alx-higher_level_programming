#!/usr/bin/python3
"""
Module that inherits from list
"""


class MyList(list):
    """ MyList class which inherits from list """
    def __init__(self, *args):
        """ init as a constructor of MyList """
        if args:
            if len(args) != 1:
                raise TypeError("Accepts one list argument")
            if not isinstance(args[0], list):
                raise TypeError("Must be a list")

    def print_sorted(self):
        """ prints the list sorted in ascending """
        sortedList = self.copy()

        for i in range(len(sortedList)):
            for j in range(i + 1, len(sortedList)):
                if sortedList[i] > sortedList[j]:
                    sortedList[i], sortedList[j] = sortedList[j], sortedList[i]
        print(sortedList)
