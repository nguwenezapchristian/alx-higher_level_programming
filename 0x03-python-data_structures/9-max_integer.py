#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    lenx = len(my_list)
    if lenx == 0:
        return None
    else:
        maxx = my_list[0]
        while i < lenx:
            if my_list[i] > maxx:
                maxx = my_list[i]
            i += 1
        return maxx
        
