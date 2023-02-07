#!/usr/bin/python3
""" Create an object from a JSON file """

import json


def load_from_json_file(filename):
    """function creates an object"""
    obj = None
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)

    return obj
