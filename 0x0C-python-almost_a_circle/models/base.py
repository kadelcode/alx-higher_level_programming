#!/usr/bin/python3
"""Base class module"""

import json


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON str repr of list)objs to a file """
        filename - cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(filename, "w") as f:
                f.write("[]")
        else:
            with open(filename, "w") as f:
                f.write(cls.to_json_string(list(map(lambda x: x.to_dictionary(), list_objs))))
