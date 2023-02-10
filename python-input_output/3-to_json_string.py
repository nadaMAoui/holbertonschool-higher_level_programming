#!/usr/bin/python3
"""main function"""

from json import dumps

def to_json_string(my_obj):
    """
    a function that returns the JSON
    representation of an object
    """
    return dumps(my_obj)
