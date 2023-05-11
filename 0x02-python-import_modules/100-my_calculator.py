#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    alist = sys.argv
    length = len(alist)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(alist[1])
        operator = alist[2]
        b = int(alist[3])
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
