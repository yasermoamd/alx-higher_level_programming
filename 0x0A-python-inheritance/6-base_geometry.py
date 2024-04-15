#!/usr/bin/python3
"""Module for the BaseGeometry class"""


class BaseGeometry:
    """Base class for geometry objects"""
    def area(self):
        """Public instance method that raises an Exception with the
            message area() is not implemented"""
        raise Exception("area() is not implemented")
