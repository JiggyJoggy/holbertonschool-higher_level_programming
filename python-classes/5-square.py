#!/usr/bin/python3
"""This module defines a square."""


class Square:
    """It represents a square."""
    __size = None

    def __init__(self, size=0):
        """Initializes size"""
        self.__size = size

    @property
    def size(self):
        """Size of square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setting size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print()
