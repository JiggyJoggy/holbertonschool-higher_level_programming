#!/usr/bin/python3
"""Save object to file"""
import json


def save_to_json_file(my_obj, filename):
    """my_obj to filename/text file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
