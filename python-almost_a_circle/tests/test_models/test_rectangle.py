#!/usr/bin/python3

"""
Unittest for rectangle
"""
import sys
import os
import io
import contextlib
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Tests for rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00(self):
        """Test 0 for Rectangle"""
        r = Rectangle(1, 2)
        self.assertEqual(isinstance(r, Base), True)

    def test_01(self):
        """Test 1 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("nan"), 1)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_02(self):
        """Test 2 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("inf"), 1)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_03(self):
        """Test 3 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_04(self):
        """Test 4 for Rectangle"""
        r = Rectangle(20, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_05(self):
        """Test 5 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_06(self):
        """Test 6 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(e.exception))

    def test_07(self):
        """Test 7 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(22, "32")
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle("10", 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r8 = Rectangle(10, 2, "3")
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, 0, "lol")
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_08(self):
        """Test 8 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 24.1)
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(9.12, 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 3, 6.7859)
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 3, 0, 6123.5)
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_09(self):
        """Test 9 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, [])
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle([1, 2, 3], 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, [[3, 4]])
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 2, 0, ["test"])
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_10(self):
        """Test 10 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, {})
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle({"3": 3, "2": 4, "1": 5}, 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, {"a": 1})
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(22, 2, 0, {"test": None})
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_12(self):
        """Test 11 for Rectangle"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -27)
        self.assertEqual(
            "height must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, -23)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -11)
        self.assertEqual(
            "x must be >= 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 5, -167)
        self.assertEqual(
            "y must be >= 0",
            str(e.exception))

    def test_13(self):
        """Test 13 for Rectangle"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(7, 0)
        self.assertEqual(
            "height must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 22)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        r = Rectangle(11, 21, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_14(self):
        """Test 14 for Rectangle"""
        r = Rectangle(3, 3)
        self.assertEqual(r.area(), 9)
        r = Rectangle(1, 22, 1)
        self.assertEqual(r.area(), 22)
        r = Rectangle(4, 12, 6, 2)
        self.assertEqual(r.area(), 48)
        r = Rectangle(9, 6, 4, 6, 12)
        self.assertEqual(r.area(), 54)

    def test_15(self):
        """Test 15 for Rectangle"""
        r = Rectangle(4, 6)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        f6 = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(s, f6)
        r = Rectangle(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        t = "##\n##\n##\n##\n"
        self.assertEqual(s, t)
        r = Rectangle(1, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        o = "#\n"
        self.assertEqual(s, o)
