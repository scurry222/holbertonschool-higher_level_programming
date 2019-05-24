#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for max_integer."""

    def test_int(self):
        self.assertEqual(max_integer([0, 1, 2, 3, 4]), 4)

    def test_not_int(self):
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_none(self):
        l = [1, 2, None]
        self.assertRaises(TypeError, max_integer, l)

    def test_negative(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_float(self):
        self.assertEqual(max_integer([3.3, 1.1, 2.2]), 3.3)

    def test_not_list(self):
        self.assertRaises(TypeError, max_integer, 7)

    def test_one(self):
        self.assertEqual(max_integer([98]), 98)
