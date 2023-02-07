#!/usr/bin/python3
""" A function that returns the json representation
    of a string
"""

import json


def to_json_string(my_obj):
    """ JSON representation of an object (string) """
    return json.dumps(my_obj)
