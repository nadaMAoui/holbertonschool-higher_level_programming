#!/usr/bin/python3
"""main Class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle
"""BaseGeometry Class"""

class Square(Rectangle):
    def __init__(self, size):
        """init"""
        super().integer_validator("size", size)
        super().__init__(size,size)
        self.__size = size
