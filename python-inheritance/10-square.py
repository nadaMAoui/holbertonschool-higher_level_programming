#!/usr/bin/python3
"""main class"""


class Square(__import__('9-rectangle').Rectangle):
    """Class BaseGeometry"""

    def __init__(self, size):
        """init"""
        super().integer_validator("size", size)
        super().__init__(size, size)
