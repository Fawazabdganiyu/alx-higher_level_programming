"""
Module Name: tests/test_models/test_rectangle.py
Description: This module provides ``rectangle`` class for testing.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Test cases for Rectagle class.
    """
    def setUp(self):
        """Setup an instance of Rectangle class"""
        self.r = Rectangle(10, 2)

    def tearDown(self):
        """Tear down the set instance"""
        pass

    def test_contructor(self):
        """Test that the instances are initiated propery.
        """
        r1 = self.r
        r2 = Rectangle(2, 10)
        r3 = Rectangle(2, 5, 3, 2)
        r4 = Rectangle(10, 2, 0, 0, 12)
        r5 = Rectangle(2, 6, id=5)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 2)
        self.assertEqual(r4.id, 12)
        self.assertEqual(r5.id, 5)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)

    def test_default_values(self):
        """Test that the optional parameters are working"""
        self.assertIsNotNone(self.r.id)
        self.assertEqual(self.r.x, 0)
        self.assertEqual(self.r.y, 0)

    def test_width_height_setter_getter(self):
        """Test that the width is set properly
        """
        self.r.width = 3
        self.r.height = 15

        self.assertEqual(self.r.width, 3)
        self.assertEqual(self.r.height, 15)

    def test_directions_setter_getter(self):
        """Test that the x and y are set properly.
        """
        self.r.x = 2
        self.r.y = 3

        self.assertEqual(self.r.x, 2)
        self.assertEqual(self.r.y, 3)

    def test_isinstance(self):
        """Test if r is an instance of Base and Rectangle"""
        self.assertIsInstance(self.r, Base)
        self.assertIsInstance(self.r, Rectangle)

    def test_no_argumemt(self):
        """Test that exception would be raised if no argument is passed"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_argument(self):
        """Test that an exception would be raised for passing one argument"""
        with self.assertRaises(TypeError):
            r = Rectangle(10)

    def test_str_width(self):
        """Test that setting width with string raises Type Error"""
        with self.assertRaises(TypeError) as message:
            Rectangle("10", 2)

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_None_width(self):
        """Test that exception is raised with None"""
        with self.assertRaises(TypeError) as message:
            self.r.width = None

    def test_dict_width(self):
        """Test that exception is raises when width = dict"""
        with self.assertRaises(TypeError) as message:
            self.r.width = {'one': 1, 'two': 2}

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_set_width(self):
        """Test that set is not validated for width"""
        with self.assertRaises(TypeError) as message:
            self.r.width = {1, 2, 3}

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_float_width(self):
        """Test that float is not validated for width"""
        with self.assertRaises(TypeError) as message:
            self.r.width = 5.5

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_list_width(self):
        """Test that list will also raise an exception
        """
        with self.assertRaises(TypeError) as message:
            self.r.width = [1, 4]

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_tuple_width(self):
        """Test that tuple also raises a Type Error
        """
        with self.assertRaises(TypeError) as msg:
            self.r.width = ("one", 2)

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_negative_width(self):
        """Test that Value Error is raised if width < 0
        """
        with self.assertRaises(ValueError) as message:
            self.r.width = -6

        self.assertEqual(str(message.exception), 'width must be > 0')

    def test_zero_width(self):
        """Test that Value Error is raised if width = 0
        """
        with self.assertRaises(ValueError) as message:
            self.r.width = 0

        self.assertEqual(str(message.exception), 'width must be > 0')

    def test_str_height(self):
        """Test that setting height with string raises Type Error"""
        with self.assertRaises(TypeError) as message:
            self.r.height = "3"

        self.assertEqual(str(message.exception), 'height must be an integer')

    def test_None_height(self):
        """Test that exception is raised with None"""
        with self.assertRaises(TypeError) as message:
            self.r.height = None

    def test_dict_height(self):
        """Test that exception is raises when height = dict"""
        with self.assertRaises(TypeError) as message:
            self.r.height = {'one': 1, 'two': 2}

        self.assertEqual(str(message.exception), 'height must be an integer')

    def test_set_height(self):
        """Test that set is not validated for height"""
        with self.assertRaises(TypeError) as message:
            self.r.height = {1, 2, 3}

        self.assertEqual(str(message.exception), 'height must be an integer')

    def test_float_height(self):
        """Test that float is not validated for height"""
        with self.assertRaises(TypeError) as message:
            self.r.height = 5.5

        self.assertEqual(str(message.exception), 'height must be an integer')

    def test_list_height(self):
        """Test that list will also raise an exception
        """
        with self.assertRaises(TypeError) as message:
            self.r.height = [1, 4]

        self.assertEqual(str(message.exception), 'height must be an integer')

    def test_tuple_height(self):
        """Test that tuple also raises a Type Error
        """
        with self.assertRaises(TypeError) as msg:
            self.r.height = ("one", 2)

        self.assertEqual(str(msg.exception), 'height must be an integer')

    def test_negative_height(self):
        """Test that Value Error is raised if height < 0
        """
        with self.assertRaises(ValueError) as message:
            self.r.height = -6

        self.assertEqual(str(message.exception), 'height must be > 0')

    def test_zero_height(self):
        """Test that Value Error is raised if width = 0
        """
        with self.assertRaises(ValueError) as message:
            self.r.height = 0

        self.assertEqual(str(message.exception), 'height must be > 0')

    def test_str_x(self):
        """Test that setting x with string raises Type Error"""
        with self.assertRaises(TypeError) as message:
            self.r.x = "2"

        self.assertEqual(str(message.exception), 'x must be an integer')

    def test_None_x(self):
        """Test that exception is raised with None"""
        with self.assertRaises(TypeError) as message:
            self.r.x = None

    def test_dict_x(self):
        """Test that exception is raises when x = dict"""
        with self.assertRaises(TypeError) as message:
            self.r.x = {'one': 1, 'two': 2}

        self.assertEqual(str(message.exception), 'x must be an integer')

    def test_set_x(self):
        """Test that set is not validated for x"""
        with self.assertRaises(TypeError) as message:
            self.r.x = {1, 2, 3}

        self.assertEqual(str(message.exception), 'x must be an integer')

    def test_float_x(self):
        """Test that float is not validated for x"""
        with self.assertRaises(TypeError) as message:
            self.r.x = 5.5

        self.assertEqual(str(message.exception), 'x must be an integer')

    def test_list_x(self):
        """Test that list will also raise an exception
        """
        with self.assertRaises(TypeError) as message:
            self.r.x = [1, 4]

        self.assertEqual(str(message.exception), 'x must be an integer')

    def test_tuple_x(self):
        """Test that tuple also raises a Type Error
        """
        with self.assertRaises(TypeError) as msg:
            self.r.x = ("one", 2)

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_negative_x(self):
        """Test that Value Error is raised when x < 0
        """
        with self.assertRaises(ValueError) as message:
            self.r.x = -3

        self.assertEqual(str(message.exception), 'x must be >= 0')

    def test_str_y(self):
        """Test that setting y with string raises Type Error"""
        with self.assertRaises(TypeError) as message:
            self.r.y = "3"

        self.assertEqual(str(message.exception), 'y must be an integer')

    def test_None_y(self):
        """Test that exception is raised with None"""
        with self.assertRaises(TypeError) as message:
            self.r.y = None

    def test_dict_y(self):
        """Test that exception is raises when y = dict"""
        with self.assertRaises(TypeError) as message:
            self.r.y = {'one': 1, 'two': 2}

        self.assertEqual(str(message.exception), 'y must be an integer')

    def test_set_y(self):
        """Test that set is not validated for y"""
        with self.assertRaises(TypeError) as message:
            self.r.y = {1, 2, 3}

        self.assertEqual(str(message.exception), 'y must be an integer')

    def test_float_y(self):
        """Test that float is not validated for y"""
        with self.assertRaises(TypeError) as message:
            self.r.y = 5.5

        self.assertEqual(str(message.exception), 'y must be an integer')

    def test_list_y(self):
        """Test that list will also raise an exception
        """
        with self.assertRaises(TypeError) as message:
            self.r.y = [1, 4]

        self.assertEqual(str(message.exception), 'y must be an integer')

    def test_tuple_y(self):
        """Test that tuple also raises a Type Error
        """
        with self.assertRaises(TypeError) as msg:
            self.r.y = ("one", 2)

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_negative_y(self):
        """Test that Value Error is raised when y < 0
        """
        with self.assertRaises(ValueError) as msg:
            self.r.y = -3

        self.assertEqual(str(msg.exception), 'y must be >= 0')
