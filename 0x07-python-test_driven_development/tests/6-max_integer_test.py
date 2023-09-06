#!/usr/bin/python3
"""
Module Name: 6-max_integer_test.py
Description: Unittest module for max_integer([..])
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test ``max_integer`` function
    """
    def test_random_integer_list(self):
        """Test random unordered integer list"""
        self.assertEqual(max_integer([2, 6, 7, 1]), 7)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_ordered_integer_list(self):
        """Test ordered integer list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_list_element(self):
        """Test list with an element"""
        self.assertEqual(max_integer([98]), 98)

    def test_int_float_mixture(self):
        """Test list with both integer and float type"""
        self.assertEqual(max_integer([2, 3, 5.5, 7.9, 8]), 8)
        self.assertEqual(max_integer([2, 3, 5.5, 7.9, 2.1]), 7.9)

    def test_empty_string(self):
        """Test empty string"""
        self.assertIsNone(max_integer(""))

    def test_string(self):
        """Test with strings"""
        self.assertEqual(max_integer("School"), "o")
        self.assertEqual(max_integer("This"), "s")

    def test_int(self):
        """Test with integer type"""
        with self.assertRaises(Exception):
            max_integer(6)

    def test_turple(self):
        """Test with turple"""
        self.assertEqual(max_integer((3, 2, 1)), 3)
