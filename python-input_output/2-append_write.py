#!/usr/bin/python3
"""main function"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added
    """
    with open(filename, encoding="UTF8", mode="a") as my_file:
        return my_file.write(text)
