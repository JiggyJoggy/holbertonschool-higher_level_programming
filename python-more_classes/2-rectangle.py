#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialization of properties"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting values"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getting height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Getting area"""
        return self.__height * self.__width

    def preimeter(self):
        """Getting perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
