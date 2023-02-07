#!/usr/bin/python3
"""A Student class module"""


class Student:
    """ A class that defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initializes class attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a json representation of Student"""
        r = {}
        for key in self.__dict__:
            value = getattr(self, key)
            if type(value) in [list, dict, str, int, bool]:
                r[key] = value
        return r
