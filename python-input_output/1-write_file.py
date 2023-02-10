#!/usr/bin/python3
def write_file(filename="", text=""):
    """
     function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    """
    with open(filename, mode="w", encoding="UTF8") as Text_File:
        return Text_File.write(str(text))
