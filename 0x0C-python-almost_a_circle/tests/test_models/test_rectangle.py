#!/usr/bin/python3
import unittest
import io
import importlib
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base
import models.rectangle

"""
Unittest for Rectangle
Including but not limited to tesing: input, output, variables
"""


class TestRectangles(unittest, testcase):

    def setUp(self):
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test__init__(self):
        rect1 = Rectangle(10,10,10,10)
        rect1.update(89)

        self.assertEqual(rect1.id, 89)
        self.assertEqual(rect1.width, 10)
        
        rect1.update(15, 2, 4, 6, 8)
        self.assertEqual(rect1.id, 15)
        self.assertEqual(rect1.width, 2)
        self.assertEqual(rect1.height, 4)
        self.assertEqual(rect1.x, 6)
        self.assertEqual(rect1.y, 8)

        self.assertRaises(ValueError, rect1.update, 9, -3, 2, 4, 6)
        with self.assertRaises(ValueError, msg = "width must be > 0")

        self.assertRaises(ValueError, rect1.update, 10, 4, -5, 4, 6)
        with self.assertRaises(ValueError, msg = "height must be > 0")

        self.assertRaises(ValueError, rect1.update, 11, 4, 8, -1, 6)
        with self.assertRaises(ValueError, msg = "x must be > 0")

        self.assertRaises(ValueError, rect1.update, 12, 4, 8, 4, -7)
        with self.assertRaises(ValueError, msg = "y must be > 0")

        self.assertRaises(TypeError, rect1.update, 13, a, 5, 4, 6)
        with self.assertRaises(TypeError, msg = "width must be an integer")

        self.assertRaises(TypeError, rect1.update, 14, 4, b, 4, 6)
        with self.assertRaises(TypeError, msg = "height must be an integer")

        self.assertRaises(TypeError, rect1.update, 15, 4, 5, x, 6)
        with self.assertRaises(TypeError, msg ="x must be an integer")

        self.assertRaises(TypeError, rect1.update, 16, 4, 5, 4, y)
        with self.assertRaises(TypeError, msg ="y must be an integer")

    def test_area(self):
        pass
    def test__str__(self):
        pass
    def test_update(self, *args, **kwargs):
        pass
    def test_display(self):
        pass

        
