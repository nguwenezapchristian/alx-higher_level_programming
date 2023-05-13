#!urs/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    a = []
    lenx = len(my_list)
    if (idx < 0 or idx > (lenx - 1)):
        return my_list
    else:
        while i < lenx:
            a.append(my_list[i])
            i += 1
        a[idx] = element
        return a
