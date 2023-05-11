#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = sys.argv
    b = len(a)
    i = 1
    total = 0
    while i < b:
        total += int(a[i])
        i += 1
    print(total)
