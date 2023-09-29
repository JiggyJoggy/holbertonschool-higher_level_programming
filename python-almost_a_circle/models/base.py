#!/usr/bin/python3
"""Classes and objects"""


__nb_objects=0


class Base():
    """Base class"""
    def __init__(self, id=None):
        """Checking id"""
        if id is not None:
            self.id = id
        else:
            __nb_objects + 1
        self.id = __nb_objects
