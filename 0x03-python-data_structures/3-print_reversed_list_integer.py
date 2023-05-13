#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0
    lenx = len(my_list)
    while i < lenx:
        print("{:d}".format(my_list[lenx - 1 - i]))
        i += 1
