#!/usr/bin/python3

"""
A function that adds 2 integers.
function prototype: def add_integer(a, b=98)
function parameters: must be integers or floats, else a TypeError is raised
"""


def add_integer(a, b=98):
    """A function that adds two(2) integers.
    Integers are of type int or float`
    """

    if type(a) == float:
        a = int(a)

    if not isinstance(a, int):
        raise TypeError('a must be an integer')

    if type(b) == float:
        b = int(b)

    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return (a + b)
