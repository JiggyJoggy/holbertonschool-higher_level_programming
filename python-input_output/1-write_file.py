#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """Write string file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
