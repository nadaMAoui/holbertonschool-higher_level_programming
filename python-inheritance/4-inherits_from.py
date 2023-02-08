#!/usr/bin/python3
"""main function"""


def inherits_from(obj, a_class):
    """
    return a boolean data_type
    if the object is an instance of a class that
    inherited from the specified class
    """
    if(isinstance(obj, a_class)) and \
       issubclass(a_class, obj.__class__) is False:
        return True
    return False
