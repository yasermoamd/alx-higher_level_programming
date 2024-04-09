#!/usr/bin/python3
"""
add_integer - function adds 2 integers.
a and b must be integers or floats, otherwise raise a TypeError
Return : a+b
"""

def add_integer(a, b=98):
    """ 
     args: (int) a, (int) b
    """

    if isinstance(a, int) not in (a, float):
        raise TypeError("a must be an integer")
    if isinstance(b, int) not in (b, float):
        raise TypeError("a must be an integer")
    a = int(a)
    b = int(b)
    return a + b
