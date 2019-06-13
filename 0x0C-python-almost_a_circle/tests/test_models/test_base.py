#!/usr/bin/python3
import unittest
from models.base import Base
"""
Unittest for the Base class
test for number of arguments
"""

class TestBase(unittest.testcase):
    def test_init(self):
        b = Base(2)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 1)
        c = Base()
        self.assertEqual(c.id, 2)

    def test.MoreArgument(self):
        with self.assertRaises(TypeError,"Too Many Arguments.")
            Base(1, 2)
    def setUp(self):
        Base.__Base__nb_objects = 0
