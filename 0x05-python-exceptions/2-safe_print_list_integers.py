#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                _value = "{:d}".format(my_list[i])
                print(_value, end='')
                count += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        raise
    finally:
        print()
    return count
