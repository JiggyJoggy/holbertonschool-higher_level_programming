#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class"""
    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Area"""
        return self.__size * self.__size
