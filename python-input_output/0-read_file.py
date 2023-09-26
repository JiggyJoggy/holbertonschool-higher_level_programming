#!/usr/bin/python3
"""File reading"""


def read_file(filename=""):
    """Reads text in a file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
