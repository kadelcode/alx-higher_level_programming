#!/usr/bin/python3

"""A class ```Square``` that inherits from Rectangle class"""

Rectangle = __import__('9-square.py').Rectangle


class Square(Rectangle):
    """Child class for ```Rectangle```"""
    def __init__(self, size):
        """Initializes the params"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Prints the desc of the `Rectangle`"""
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string
