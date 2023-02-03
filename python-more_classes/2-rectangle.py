#!/usr/bin/python3
""" this is the main rectangle class """


class Rectangle:
    """ class Reactangle"""

    def __init__(self, width=0, height=0):
        """initi"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ function returns width of rectangle"""
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ function that returns height of rectangle"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method returns rectangle area"""
        return self.width * self.__height
    
    def perimeter(self):
        """mathod return rectangle perimeter"""
        if (self.area() is 0):
            return 0
        else:
            return self.__width * 2 + self.__height * 2
    