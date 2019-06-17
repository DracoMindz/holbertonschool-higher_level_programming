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

        self.assertRaises(ValueError, rect1.update, 9,-3, 2, 4, 6)
        with self.assertRaises(ValueError, msg = "width must be > 0")
    def test__str__(self):
        pass
    def test_update(self, *args, **kwargs):
        pass
