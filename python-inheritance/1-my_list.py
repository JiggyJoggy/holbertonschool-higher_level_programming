#!/usr/bin/python3
"""MyList inherits list"""


class MyList(list):
    """Class for list"""

    def print_sorted(self):
        """Sorts list"""
        print(sorted(self))
