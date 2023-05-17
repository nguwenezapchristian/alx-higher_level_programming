#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keyz = list(a_dictionary)
    for i in keyz:
        if i == key:
            del a_dictionary[key]
    return a_dictionary

