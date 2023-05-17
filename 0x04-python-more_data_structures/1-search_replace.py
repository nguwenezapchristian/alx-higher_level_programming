#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    my_list_0 = my_list[:]
    while i < len(my_list_0):
        if my_list_0[i] == search:
            my_list_0[i] = replace
        i += 1
    return my_list_0
