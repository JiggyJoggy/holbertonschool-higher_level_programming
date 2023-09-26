#!/usr/bin/python3
"""Append a file"""


def append_write(filename="", text=""):
    """Append a text/string at the end of a text file/filename"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
