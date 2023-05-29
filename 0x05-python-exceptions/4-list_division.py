#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        listDivision = []
        for i in range(list_length):
            try:
                element = my_list_1[i] / my_list_2[i]
                listDivision.append(element)
            except ZeroDivisionError:
                listDivision.append(0)
                print("division by 0")
            except TypeError:
                listDivision.append(0)
                print("wrong type")
    except IndexError:
        listDivision.append(0)
        print("out of range")
    finally:
        return listDivision
