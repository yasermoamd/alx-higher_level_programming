#!/usr/bin/python3
"""Module for the is_same_class function"""


def is_same_class(obj, a_class):
    """Write a function that returns True if the object is exactly
        an instance of the specified class ; otherwise False."""
    if type(obj) is a_class:
        return True
    return False
