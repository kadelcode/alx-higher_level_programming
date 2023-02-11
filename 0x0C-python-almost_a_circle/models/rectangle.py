#!/usr/bin/python3
"""Rectangle class module"""

class Rectangle(Base):
    """A Rectangle classs"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class variables"""
        super.__init__()
        self.__width = width
        self.height = height
        self.x = x
        self.y = y
