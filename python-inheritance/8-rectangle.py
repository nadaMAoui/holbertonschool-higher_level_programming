#!/usr/bin/python3
"""main Class"""


class BaseGeometry():
    """BaseGeometry Class"""

    def area(self):
        """raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if(type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if(value <= 0):
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """ init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
