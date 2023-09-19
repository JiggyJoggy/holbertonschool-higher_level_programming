#!/usr/bin/python3
"""Prints a square with the character #"""


def print_square(size):
    """Function that prints out the square using the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
            for row in range(size):
                for col in range(size):
                    print("#", end="")
                print()
