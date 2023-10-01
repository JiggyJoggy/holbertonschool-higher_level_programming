#!/usr/bin/python3
"""Classes and objects"""
import json


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Checking id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            json_str = cls.\
                to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            json_string = []
        return json.loads(json_string)
