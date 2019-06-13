#!/usr/bin/python3
""" Tests for base and base functions """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_base(unittest.TestCase):
    """ Test for Base class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test id functionality """

        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(4)
        self.assertEqual(b.id, 4)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(333)
        self.assertEqual(b.id, 333)
        b = Base(-2)
        self.assertEqual(b.id, -2)

    def test_type(self):
        """ Test type and instance """

        b = Base()
        self.assertEqual(type(b), Base)
        self.assertTrue(isinstance(b, Base))

    def test_to_json_string(self):
        """ Test to_json_string functionality """

        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_d = Base.to_json_string([d])

        self.assertTrue(isinstance(d, dict))

        self.assertTrue(isinstance(json_d, str))

        self.assertCountEqual(
            json_d, '{["id": 1, "x": 2, "y": 3, "width": 4, "height": 5]}')

        json_d = Base.to_json_string([])
        self.assertEqual(json_d, "[]")

        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")

        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Base.to_json_string("str")

        with self.assertRaises(TypeError):
            Base.to_json_string(["list", "strings"])

        with self.assertRaises(TypeError):
            Base.to_json_string(1.2)

        with self.assertRaises(TypeError):
            Base.to_json_string([1, 2, 3, 4])

        with self.assertRaises(TypeError):
            Base.to_json_string({1: 'dict', 2: 'value'})

        with self.assertRaises(TypeError):
            Base.to_json_string((0, 0))

        with self.assertRaises(TypeError):
            Base.to_json_string([{1, 2}], [{3, 4}])

    def test_save_to_file(self):
        """Test class method save_to_file with normal types."""
        with self.assertRaises(AttributeError):
            Base.save_to_file([Base(1), Base(2)])

        with self.assertRaises(TypeError):
            Rectangle.save_to_file(1, 2)

        with self.assertRaises(TypeError):
            Rectangle.save_to_file(1.2)

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_from_json_string(self):
        """ Test from_json_string functionality """

        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

        with self.assertRaises(TypeError):
            Rectangle.from_json_string("Hi", 98)

        list_in = [
            {'id': 2, 'width': 2, 'height': 4},
            {'id': 5, 'width': 3, 'height': 6}
        ]
        json_in = Rectangle.to_json_string(list_in)
        json_out = Rectangle.from_json_string(json_in)
        self.assertEqual(type(json_out), list)

        with self.assertRaises(TypeError):
            l = Rectangle.from_json_string([1, 2])

        with self.assertRaises(TypeError):
            l = Rectangle.from_json_string(1)

        with self.assertRaises(TypeError):
            l = Rectangle.from_json_string(1.2)

        with self.assertRaises(TypeError):
            l = Rectangle.from_json_string((8, 9))

        with self.assertRaises(TypeError):
            l = Rectangle.from_json_string({1: 'value', 2: 'dict'})

    def test_create(self):
        """ Test create functionality """
        with self.assertRaises(TypeError):
            err = Rectangle.create("str")

    def test_load_from_file(self):
        """Test load_from_file functionality """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        if os.path.exists("Base.json"):
            os.remove("Base.json")

        r_output = Rectangle.load_from_file()
        self.assertEqual(r_output, "[]")

        sq_output = Square.load_from_file()
        self.assertEqual(sq_output, "[]")

        with self.assertRaises(TypeError):
            list_rectangles_output = Rectangle.load_from_file("str")

if __name__ == '__main__':
    unittest.main()
