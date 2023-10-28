#!/usr/bin/python3
def add_integer(a, b=98):
    """ adds two integers and returns a sum
    Args:
        a(int): first argument
        b(int): second argument
    """
    if isinstance(a, float) and a+1 == a:
        raise OverflowError("a is too large")
    if isinstance(b, float) and b+1 == b:
        raise OverflowError("b is too large")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
