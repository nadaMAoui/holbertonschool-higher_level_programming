#!/usr/bin/python3
"""main function"""


def is_kind_of_class(obj, a_class):
    """
    return a boolean data_type if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
    """
    return(isinstance(obj, a_class))
