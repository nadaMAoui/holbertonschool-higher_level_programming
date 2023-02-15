#!/usr/bin/python3
"""
model class that holds the base class to manager all
the id attributes of all classesthat extend from the
base class to avoid duplication of same code
"""


class Base(self):
    """base classe"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""

        if(id is None)
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id   
