#!/usr/bin/python3
"""main class"""


class Square(__import__('9-rectangle').Rectangle):
    """Class BaseGeometry"""

    def __init__(self, size):
        """init"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return area size"""
        return self.__size * self.__size

    def __str__(self):
        """Return the following aquare description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
