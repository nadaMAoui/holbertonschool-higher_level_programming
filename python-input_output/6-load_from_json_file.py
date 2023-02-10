#!/usr/bin/python3
"""main function"""

from json import loads


def load_from_json_file(filename):
    """
    a function that creates
    an Object from a “JSON file”
    """
    with open(filename, encoding="UTF8") as myfile:
        return loads(myfile.read())
