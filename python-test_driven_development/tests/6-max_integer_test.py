#!/usr/bin/python3
"""Unittest for max_integer([])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_max_integer(unittest.TestCase):
    """Max at the end"""
    def test_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    """Max at the beginning"""
    def text_start(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    """Max in the middle"""
    def test_middle(self):
        self.assertEqual(max_integer([2, 3, 1]), 3)

    """One negative number in the list"""
    def test_one_negative(self):
        self.assertEqual(max_integer([-1, 2, 3, 5]), 5)

    """Only negative numbers in the list"""
    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    """List of one element"""
    def test_one_int(self):
        self.assertEqual(max_integer([80]), 80)

    """List is empty"""
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
