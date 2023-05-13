#!urs/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    a = my_list[:]
    lenx = len(my_list)
    if (idx < 0 or idx > (lenx - 1)):
        return my_list
    else:
        a[idx] = element
        return a
