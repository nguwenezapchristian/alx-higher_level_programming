#!/usr/bin/python3
def remove_char_at(str, n):
    string = []
    for i in range(len(str)):
        if n >= len(str) or n < 0:
            string.append(str[i])
        elif str[i] == str[n]:
            continue
        else:
            string.append(str[i])
    nstr = "".join(string)
    return nstr
