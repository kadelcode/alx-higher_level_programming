#!/usr/bin/python3
"""Implementation of Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Child class of Rectangle class"""
    def __init__(self, size):
        """Initializes the values"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
