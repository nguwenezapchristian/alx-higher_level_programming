#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = sys.argv
    b = len(a) - 1
    if b == 0:
        print("{} arguments.".format(b))
    elif b == 1:
        print("{} argument:".format(b))
    else:
        print("{} arguments:".format(b))
    i = 1
    while i <= b:
        print("{}: {}".format(i, a[i]))
        i += 1
