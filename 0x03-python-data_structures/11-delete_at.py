#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lenx = len(my_list)
    if 0 > idx > (lenx - 1):
        return my_list
    else:
        del my_list[idx]
        return my_list
