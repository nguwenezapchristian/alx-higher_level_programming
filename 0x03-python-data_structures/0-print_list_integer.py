#!/usr/bin/python3
if __name__ == "__main__":
    def print_list_integer(my_list=[]):
        length = len(my_list)
        i = 0
        while i < length:
            print("{}".format(my_list[i]))
            i += 1
