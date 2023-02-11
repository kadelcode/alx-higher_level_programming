#!/usr/bin/python3
"""Rectangle class module"""

class Rectangle(Base):
    """A Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class variables"""
        super.__init__(id)
        self.__width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        self.__width = value

    @property
    def height(self):
        """getter for the height"""
        return self.__height
