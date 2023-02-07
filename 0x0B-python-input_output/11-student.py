#!/usr/bin/python3
"""`Student` class module"""


class Student:
    """A class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a json representation of Student"""
        r = {}
        if attrs is not None:
            keys = [key for key in self.__dict__ if key in attrs]
        else:
            keys = [key for key in self.__dict__]

        for key in keys:
            value = getattr(self, key)
            if type(value) in [list, dict, str, int, bool]:
                r[key] = value
        return r

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance from json"""
        for key in json:
            setattr(self, key, json[key])
