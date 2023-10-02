#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
"""Unittest classes"""


class TestBase(unittest.TestCase):
    '''The subclass of the TestCase to test Base'''

    def test_id(self):
        '''Testing the __init__ method id'''
        b1 = Base(1)
        self.assertEqual(b1.id, 1)