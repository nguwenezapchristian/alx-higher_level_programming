#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    keyz = list(a_dictionary)
    for i in keyz:
        if i == key:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
    return a_dictionary
