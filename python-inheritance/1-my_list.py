#!/usr/bin/python3
""" main class"""


class MyList(list):
    """My_List class"""
    def print_sorted(self):
        """ method to print sorted list"""
        print(sorted(self))
