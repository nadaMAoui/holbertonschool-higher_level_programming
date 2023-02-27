#!/usr/bin/python3
"""A module to add two numbers
This module performs the addition operation between two numbers,
these numbers can be integers or floats.
"""


def add_integer(a, b=98):
    """add two numbers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = cover_to_int(a)
    b = covr_to_int(b)
    return a + b


def convert_to_int(num):
    """Cast the data type of num
    """
    if type(num) is float:
        num = int(num)
        return num

    return num
