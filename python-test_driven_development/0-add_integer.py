#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """
    Adds two ints and returns sum as an int

    Raises:
    TypeError: if 'a' or 'b' is not an int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(round(a + b))
