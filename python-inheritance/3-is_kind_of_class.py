#!/usr/bin/python3
"""Checking object of an instance or inherited"""


def is_kind_of_class(obj, a_class):
    """Checking object"""
    return isinstance(obj, a_class) or issubclass(obj.__class__, a_class)
