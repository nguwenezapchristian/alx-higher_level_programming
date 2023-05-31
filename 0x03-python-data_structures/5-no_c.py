#!/usr/bin/python3
def no_c(my_string):
    string = []
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            string.append(my_string[i])
    nstr = ''.join(string)
    return nstr
