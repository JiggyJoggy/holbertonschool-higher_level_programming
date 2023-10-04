#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
"""Unittest classes"""


class TestBase_init(unittest.TestCase):
    """The subclass of the TestCase to test Base"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_unique(self):
        """Testing the __init__ method id"""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_id_mult_obj(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_mix_obj(self):
        """test number of obj"""
        base1 = Base()
        base3 = Base(29)
        base4 = Base()
        self.assertEqual(base1.id, base4.id - 1)

    def test_None(self):
        """Test none"""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_negative_id(self):
        """negative id"""
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)

    def test_string_id(self):
        """string id"""
        b1 = Base("Holberton")
        self.assertEqual(b1.id, "Holberton")
        b2 = Base("1")
        self.assertEqual(b2.id, "1")

    def test_float_id(self):
        """float id"""
        b1 = Base(1.1)
        self.assertEqual(b1.id, 1.1)

    def test_bool_id(self):
        """bool id"""
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_list_F_id(self):
        """bool id"""
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_list_id(self):
        """bool id"""
        b1 = Base([1, ])
        self.assertEqual(b1.id, [1, ])

    def test_tuple_id(self):
        """tuple id"""
        b1 = Base((1))
        self.assertEqual(b1.id, (1))

    def test_tuple_m_id(self):
        """tuple id"""
        b1 = Base((1, 2, 3))
        self.assertEqual(b1.id, (1, 2, 3))

    def test_dict_id(self):
        """dict id"""
        b1 = Base({'1': 2})
        self.assertEqual(b1.id, {'1': 2})

    def test_set_id(self):
        """set id"""
        b1 = Base({2})
        self.assertEqual(b1.id, {2})

    def test_complex(self):
        """test id"""
        b = Base(complex(10))
        self.assertEqual(b.id, complex(10))

    def test_froze_set(self):
        """test id"""
        b = Base(frozenset({1, 2, 3}))
        self.assertEqual(b.id, frozenset({1, 2, 3}))

    def test_float_inf(self):
        """test id"""
        b = Base(float('inf'))
        self.assertEqual(b.id, float('inf'))

    def test_nan(self):
        b = Base(float('nan'))
        self.assertNotEqual(b.id, float('nan'))

    def test_wr_arg(self):
        """many args"""
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_private_access(self):
        """test accessing private attributes"""
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects
        with self.assertRaises(AttributeError):
            b.nb_objects

    def test_change_id(self):
        """change id"""
        base = Base(20)
        base.id = 15
        self.assertEqual(base.id, 15)

class TestBase_to_json_string(unittest.TestCase):
    """Test to json string"""

    def test_more_args(self):
        """test more args"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 0)
