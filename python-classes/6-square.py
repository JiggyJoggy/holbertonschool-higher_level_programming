#!/usr/bin/python3
"""This module defines a square."""


class Square:
    """It represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes size & pos"""
        self.__size = size
        self.position = position

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
        else:
            self.__size = size

    @property
    def position(self):
        """Gets pos"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets pos"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(elem, int) for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(elem >= 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print()
            return
        for index in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for index_2 in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print()
