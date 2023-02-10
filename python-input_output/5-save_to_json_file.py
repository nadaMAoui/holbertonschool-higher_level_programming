#!/usr/bin/python3
"""main function"""

from json import dumps


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text
    file, using a JSON representation
    """
    with open(filename, encoding="UTF8", mode="w") as myfile:
        myfile.write(dumps(my_obj))
