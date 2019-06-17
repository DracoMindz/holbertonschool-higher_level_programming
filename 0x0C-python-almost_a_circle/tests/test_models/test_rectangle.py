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
Including but not limited to tesing: input, output, variables)
"""


class TestRectangles(unittest, testcase):

    def setUp(self):
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_init(self):
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

    def test_area(self):
        pass
    def test__str__(self):
        pass
    def test_update(self, *args, **kwargs):
        pass
    def test_display(self):
        pass

        
