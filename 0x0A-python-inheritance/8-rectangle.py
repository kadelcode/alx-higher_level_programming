#!/usr/bin/python3
"""A class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Initialize rectangle value"""
    self.integer_validator("width", width)
    self.__width = width
    self.integer_validator("height", height)
    self.__height = height
