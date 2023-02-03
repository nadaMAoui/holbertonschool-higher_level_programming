#!/usr/bin/python3
""" this is the main rectangle class """


class Rectangle:
    """ class Reactangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initi"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
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

    def __str__(self):
        new_str = ""
        if (self.width is 0 or self.height is 0):
            return(new_str)
        else:
            return"\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """returns a string representation of rectangle"""
        w = str(eval('self.width'))
        h = str(eval('self.height'))
        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        """prints message when rectangle instence is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
