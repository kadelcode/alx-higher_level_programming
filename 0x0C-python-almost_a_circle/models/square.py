#!/usr/bin/python3
""" square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes class attributes """
        super().__init__(size, size, x, y, id)
