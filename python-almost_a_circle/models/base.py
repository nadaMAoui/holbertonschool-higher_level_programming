#!/usr/bin/python3
"""
A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.
"""

from os import path
import json


class Base:
    """
    base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
