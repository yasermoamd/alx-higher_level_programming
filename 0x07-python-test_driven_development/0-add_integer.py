#!/usr/bin/python3

def add_integer(a, b=98):
    """ function add tow integer """
    try:
        if type(a) not in (int, float):
            raise TypeError("a must be an integer")
        if type(b) not in (int, float):
            raise TypeError("a must be an integer")
        else:
            return a + b
    except TypeError:
        raise TypeError("a must be an integer")


