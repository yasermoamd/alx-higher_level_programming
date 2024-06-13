#!/usr/bin/python3
"""Module for the Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation function for Square class"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method that returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Method that returns  the square description
            [Squre] <width>/<height>"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
