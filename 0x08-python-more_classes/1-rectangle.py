#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by
Private instance attributes: width & height
Both width & height are integers
"""
class Rectangle:
    """
    Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes class parameters.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter returns width"""
        self.width = width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise Value("width must be >= 0")
        self.__width = value
