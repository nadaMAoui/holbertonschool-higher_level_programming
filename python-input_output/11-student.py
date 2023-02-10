#!/usr/bin/python3
"""main class"""


class Student():
    """ class student"""

    def __init__(self, first_name, last_name, age):
        """Init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Attributes"""
        if attrs is not None:
            new_attrs = {}
            for i in attrs:
                if i is "first_name":
                    new_attrs[i] = self.first_name
                elif i is "last_name":
                    new_attrs[i] = self.last_name
                elif i is "age":
                    new_attrs[i] = self.age
                else:
                    pass
            return new_attrs
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attrs of student instance"""
        for key, value in json.items():
            setattr(self, key, value)
