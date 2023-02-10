#!/usr/bin/python3
from json import dumps
"""main function"""

def to_json_string(my_obj):
    """
    a function that returns the JSON
    representation of an object
    """
    return dumps(my_obj)
