#!/usr/bin/python3
"""Module for the BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry objects"""
    def area(self):
        """Public instance method that raises an Exception with the
            message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
