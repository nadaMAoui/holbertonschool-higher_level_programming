#!/usr/bin/python3
"""main function"""


def class_to_json(obj):
    """
    a function that returns the dictionary description
    with simple data structure for JSON serialization
    of an object
    """
    return (obj.__dict__)
