#!/usr/bin/python3

""" A function that checks exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """ check if the object is exactly an instance of the specified class"""
    if isinstance(obj, a_class):
        return True

    else:
        return False
