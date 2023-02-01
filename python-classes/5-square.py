#!/usr/bin/python3
""" define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ size private attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """type public attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """current square area"""
        return(self.__size ** 2)

    def my_print(self):
        """print a # square"""
        if self.__size == 0:
            print()
        else:
            for i in range (self.__size):
                for j in range (self.__size):
                    print("#", end="")
                print()
