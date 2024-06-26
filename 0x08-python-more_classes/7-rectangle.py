#!/usr/bin/python3
"""this is a program that have a class with private attributes"""


class Rectangle:
    """a class have:
    args: (int) width, (int) height
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the size instance attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the width instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the size instance attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function to calculate the area"""

        return self.__width * self.__height

    def perimeter(self):
        """function to calculate the perimeter of retangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for i in range(self.__height)])

    def __repr__(self):
        """string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete the instance and print the blow message when delelte it"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
