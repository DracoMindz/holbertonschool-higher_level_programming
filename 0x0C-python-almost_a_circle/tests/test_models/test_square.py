#!/usr/bin/python3
import unittest
import io
import importlib
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import models.square

"""
Unittest for Square
Including but not limited to testing: imput, output, variables
"""

class TestSquares(unittest, testcase):

    def setUp(self):
        importlib.reload(models.square)
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test__init__(self):
        sq1 = Square(6, 2, 2, 33)
        sq1.update(89)

        self.assertEqual(sq1.id, 89)
        self.assertEqual(sq1.width, 10)

        sq1.update(4, 6, 5, 15)
        self.assertEqual(sq1.id, 15)
        self.assertEqual(sq1.size, 4)
        self.assertEqual(sq1.x, 6)
        self.assertEqual(sq1.y, 7)

        self.assertRaises(ValueError, sq1.update, -9, 3, 2, 1)
        with self.assertRaises(ValueError, msg = "size must be > 0")
        self.assertRaises(ValueError, sq1.update, 5, -3, 2, 2)
        with self.assertRaises(ValueError, msg = "x must be > 0")
        self.assertRaises(ValueError, sq1.update, 5, 3, -2, 3)
        with self.assertRaises(ValueError, msg = "y must be > 0")

        self.assertRaises(TypeError, sq1.update, a, 5, 4, 4)
        with self.assertRaises(TypeError, msg = "size must be an integer")
        self.assertRaises(TypeError, sq1.update, 5, b, 4, 5)
        with self.assertRaises(TypeError, msg = "x  must be an integer")
        self.assertRaises(TypeError, sq1.update, 5, 3, w, 6)
        with self.assertRaises(TypeError, msg = "y  must be an integer")

    def test__str__(self):
        pass
    def test_update(self, *args, **kwargs):
        pass
