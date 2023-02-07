#!/usr/bin/python3
"""A function that adds a new attribute to an object"""


def add_attribute(self, attribute, value):
    """Adds attribute if possible"""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
