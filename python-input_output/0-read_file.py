#!/usr/bin/python3
"""main function"""


def read_file(filename=""):
    """
    a function that reads a text 
    file (UTF8) and prints it to stdout
    """
    with open(filename, mode = "r", encoding="UTF8") as My_File:
        for line in My_File:
            print(line, end='')
