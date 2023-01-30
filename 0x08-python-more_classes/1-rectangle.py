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
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter gets the height"""
        self.height = height

    @height.setter
    def height(self, value):
        """Setter sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
