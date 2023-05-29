#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numberOfElement = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            numberOfElement += 1
    except IndexError:
        pass
    except TypeError:
        pass
    finally:
        print()
        return numberOfElement
