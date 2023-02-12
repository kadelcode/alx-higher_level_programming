#!/usr/bin/python3
""" square.py """

from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes class attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
