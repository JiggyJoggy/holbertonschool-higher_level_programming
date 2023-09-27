#!/usr/bin/python3
"""Adds items to a files"""
from sys import argv
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    mylist = load('add_item.json')
except FileNotFoundError:
    mylist = []
finally:
    save(mylist + argv[1:], 'add_item.json')
