#!/usr/bin/python3
"""Subclass of"""

def inherits_from(obj, a_class):
    """Checking"""
    if isinstance(obj, a_class) and not issubclass(a_class, obj.__class__):
        return True
    return False
