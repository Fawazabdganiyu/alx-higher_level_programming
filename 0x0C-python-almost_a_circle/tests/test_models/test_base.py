"""
Module Name: tests/test_models/test_base.py
Description: This module provide ``base`` class for testing
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A simple TestBase class definition
    """

    def test_default_id(self):
        """Test that the default id is incremented correctly.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1, "First instance should have id 1")
        self.assertEqual(b2.id, 2, "Second instance should have id 2")

    def test_specified_id(self):
        """Test that the specified id is assigned correctly.
        """
        b3 = Base(12)
        self.assertEqual(b3.id, 12, "Specified id should be assigned")

    def test_mixed_id_behaviour(self):
        """Test that the default id continues sequencially when another id is
        specified.
        """
        b4 = Base()
        b5 = Base(6)
        b6 = Base()
        self.assertEqual(b4.id, 3, "The next instance id should be 3")
        self.assertEqual(b5.id, 6, "Specified id should be assigned")
        self.assertEqual(b6.id, 4, "Next instance id be 4")
