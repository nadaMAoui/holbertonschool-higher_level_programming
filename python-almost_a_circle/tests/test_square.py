#!/usr/bin/python3
"""Defines unittests for models/square.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.square import square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_square_is_base(self):
        self.assertIsInstance(Rectangle(1, 2), Base)

