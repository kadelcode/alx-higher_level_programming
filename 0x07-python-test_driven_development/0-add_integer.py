#!/usr/bin/python3

"""
A function that adds 2 integers.
function prototype: def add_integer(a, b=98)
function parameters: must be integers or floats, else a TypeError is raised
float parameters are casted to integers

"""

def add_integer(a, b=98):
    """
    A function that adds two(2) integers.
    Integers are of type int or float

    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError('a must be an integer')

    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError('b must be an integer')

    return (a + b)
