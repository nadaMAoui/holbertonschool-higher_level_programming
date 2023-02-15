#!/usr/bin/python3
"""
model class that holds the base class to manager all
the id attributes of all classesthat extend from the
base class to avoid duplication of same code
"""
import os


class Base(self):
    """base classe"""

    __nb_objects = 0
    id : int
    def __init__(self, id=None):
        if(id is None)
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id   
