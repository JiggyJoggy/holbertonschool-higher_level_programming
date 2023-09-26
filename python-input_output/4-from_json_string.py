#!/usr/bin/python3
"""JSON"""
import json


def from_json_string(my_str):
    """Returns an object by JSON str"""
    return json.loads(my_str)
