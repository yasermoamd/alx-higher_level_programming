#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation function for Rectangle class"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method that returns a string representation of the rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
