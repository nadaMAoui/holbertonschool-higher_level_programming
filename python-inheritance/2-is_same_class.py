#!/usr/bin/python3
""" function"""


def is_same_class(obj, a_class):
    """
    return boolean data_type if the obj is
    an instance of the specified class
    """
    return (type(obj) is (a_class))
