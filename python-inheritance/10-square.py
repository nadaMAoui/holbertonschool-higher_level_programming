#!/usr/bin/python3
"""main Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""BaseGeometry class"""

Rectangle = __import__('9-rectangle').Rectangle
"""Rectangle Class"""

class Square(Rectangle):
    def __init__(self, size):
        """init"""
        self().integer_validator("size", size)
        super().__init__(size,size)
        self.__size = size
