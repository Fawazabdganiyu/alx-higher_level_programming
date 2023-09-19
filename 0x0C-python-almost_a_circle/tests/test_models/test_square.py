"""
Module Name: tests/test_models/test_square.py
Description: This module defines ``Square`` class for testing.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
import unittest
from models.square import Square
from models.base import Base
from io import StringIO
import sys


class TestSquareClass(unittest.TestCase):
    """Test cases for Rectagle class.
    """
    def setUp(self):
        """Setup an instance of Rectangle class"""
        self.r = Square(10)

    def tearDown(self):
        """Tear down the set instance"""
        pass

    def test_contructor(self):
        """Test that the instances are initiated propery.
        """
        r1 = self.r
        r2 = Square(2)
        r3 = Square(2, 5, 3)
        r4 = Square(10, 2, 0, 12)
        r5 = Square(2, 6, id=5)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 3)
        self.assertEqual(r4.id, 12)
        self.assertEqual(r5.id, 5)
        self.assertEqual(r5.x, 6)
        self.assertEqual(r5.y, 0)

    def test_default_values(self):
        """Test that the optional parameters are working"""
        self.assertIsNotNone(self.r.id)
        self.assertEqual(self.r.x, 0)
        self.assertEqual(self.r.y, 0)

    def test_size_setter_getter(self):
        """Test that the width is set properly
        """
        self.r.size = 3

        self.assertEqual(self.r.size, 3)

    def test_directions_setter_getter(self):
        """Test that the x and y are set properly.
        """
        self.r.x = 2
        self.r.y = 3

        self.assertEqual(self.r.x, 2)
        self.assertEqual(self.r.y, 3)

    def test_isinstance(self):
        """Test if r is an instance of Base and Square"""
        self.assertIsInstance(self.r, Base)
        self.assertIsInstance(self.r, Square)

    def test_no_argumemt(self):
        """Test that exception would be raised if no argument is passed"""
        with self.assertRaises(TypeError):
            r = Square()

    def test_one_argument(self):
        """Test that an exception is not raised for passing one argument"""
        r = Square(10)

        self.assertEqual(r.size, 10)

    def test_str_width(self):
        """Test that setting width with string raises Type Error"""
        with self.assertRaises(TypeError) as message:
            Square("10", 2)

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_None_size(self):
        """Test that exception is raised with None"""
        with self.assertRaises(TypeError) as message:
            self.r.size = None

    def test_dict_size(self):
        """Test that exception is raises when width = dict"""
        with self.assertRaises(TypeError) as message:
            self.r.size = {'one': 1, 'two': 2}

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_set_size(self):
        """Test that set is not validated for width"""
        with self.assertRaises(TypeError) as message:
            self.r.size = {1, 2, 3}

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_float_size(self):
        """Test that float is not validated for width"""
        with self.assertRaises(TypeError) as message:
            self.r.size = 5.5

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_list_size(self):
        """Test that list will also raise an exception
        """
        with self.assertRaises(TypeError) as message:
            self.r.size = [1, 4]

        self.assertEqual(str(message.exception), 'width must be an integer')

    def test_tuple_size(self):
        """Test that tuple also raises a Type Error
        """
        with self.assertRaises(TypeError) as msg:
            self.r.size = ("one", 2)

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_negative_size(self):
        """Test that Value Error is raised if width < 0
        """
        with self.assertRaises(ValueError) as message:
            self.r.size = -6

        self.assertEqual(str(message.exception), 'width must be > 0')

    def test_zero_size(self):
        """Test that Value Error is raised if width = 0
        """
        with self.assertRaises(ValueError) as message:
            self.r.size = 0

        self.assertEqual(str(message.exception), 'width must be > 0')

    def test_private_size(self):
        """Test that width is private
        """
        with self.assertRaises(AttributeError):
            self.r.__width

    def test_private_height(self):
        """Test that height is private
        """
        with self.assertRaises(AttributeError):
            self.r.__height

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

    def test_private_x(self):
        """Test that x is private
        """
        with self.assertRaises(AttributeError):
            self.r.__x

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

    def test_private_y(self):
        """Test that __y is private
        """
        with self.assertRaises(AttributeError):
            self.r.__y

    def test_area_value(self):
        """Test that area returns the correct value
        """
        self.r.size = 3

        self.assertAlmostEqual(self.r.area(), 9)

        self.r.size = 10

        self.assertAlmostEqual(self.r.area(), 100)

    def test_area_value_with_coordinate(self):
        """Test that the coordinates do not affect the area value
        """
        r = Square(8, 7, 3, 4)

        self.assertAlmostEqual(r.area(), 64)

    def test_area_value_with_id(self):
        """Test that id do not affect area value
        """
        r = Square(8, 7, id=12)

        self.assertAlmostEqual(r.area(), 64)

    def test_area_value_with_all(self):
        """Test that area value is independent of any other parameters
        aside width and height
        """
        r = Square(7, 78, 10, 5)

        self.assertAlmostEqual(r.area(), 49)

    def test_area_with_argument(self):
        """Test that area with any argument raises an exception
        """
        with self.assertRaises(TypeError):
            self.r.area(1)

        with self.assertRaises(TypeError):
            self.r.area(3, 4)

    @staticmethod
    def capture_stdout(obj):
        """captures the stdout for testing

        Args:
            obj (obj): The instance to test for display method

        Return (obj): The captured stdout

        """
        # Redirect the standard output to capture printed instance
        stdout = StringIO()
        sys.stdout = stdout

        obj.display()

        # Restore the standard output
        sys.stdout = sys.__stdout__

        return stdout

    def test_display_method(self):
        """Test that the character # is printed to stdout as the Square
        instance.
        """
        r = Square(4)
        r2 = Square(2)

        expected = '####\n####\n####\n####\n'
        stdout = TestSquareClass.capture_stdout(r)
        captured = stdout.getvalue()
        self.assertEqual(expected, captured)

        expected = '##\n##\n'
        stdout = TestSquareClass.capture_stdout(r2)
        captured = stdout.getvalue()
        self.assertEqual(expected, captured)

    def test_display_one_argument(self):
        """Test that passing argument in display raises exception
        """
        with self.assertRaises(TypeError):
            self.r.display(4)

    def test_display_with_two_parameter(self):
        """Test that TypeError is raised with two argument.
        """
        with self.assertRaises(TypeError):
            self.r.display(2, 6)

    def test_display_with_zero_width_height(self):
        """Test that value error is raised with width = height = 0 for display.
        """
        with self.assertRaises(ValueError) as msg:
            r = Square(0)

        self.assertEqual(str(msg.exception), 'width must be > 0')

    def test_display_x(self):
        """Test x coordinate with display.
        """
        r = Square(2, x=3)

        expected = '   ##\n   ##\n'
        stdout = TestSquareClass.capture_stdout(r)
        captured = stdout.getvalue()

        self.assertEqual(expected, captured)

    def test_display_y(self):
        """Test y coordinate with display.
        """
        r = Square(2, y=3)

        expected = '\n\n\n##\n##\n'
        stdout = TestSquareClass.capture_stdout(r)
        captured = stdout.getvalue()

        self.assertEqual(expected, captured)

    def test_display_x_y(self):
        """Test that both x and y works as expected with display.
        """
        r = Square(2, 2, 2)

        expected = '\n\n  ##\n  ##\n'
        stdout = TestSquareClass.capture_stdout(r)
        captured = stdout.getvalue()

        self.assertEqual(expected, captured)

    def test_dispaly_x_y_id(self):
        """Test all parameter with display method
        """
        r = Square(2, 2, 2, 45)

        expected = '\n\n  ##\n  ##\n'
        stdout = TestSquareClass.capture_stdout(r)
        captured = stdout.getvalue()

        self.assertEqual(expected, captured)

    def test_str_width_height(self):
        """Test that the string is represented well with only
        default value
        """
        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 0/0 - 10')

    def test_str_all(self):
        """Test that all parameters are have correct string representation
        """
        r = Square(4, 2, 1, 12)

        self.assertEqual(str(r), f'[Square] (12) 2/1 - 4')

    def test_str_x(self):
        """Test that only x is represented with instance.
        """
        self.r.x = 4

        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 4/0 - 10')

    def test_str_y(self):
        """Test that only y is represented with the instance.
        """
        self.r.y = 4

        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 0/4 - 10')

    def test_str_id(self):
        """Test that only id s represented well with the instance.
        """
        self.r.id = 89

        self.assertEqual(str(self.r), f'[Square] (89) 0/0 - 10')

    def test_str_x_y(self):
        """Test that x and y are represented with  the instance well.
        """
        r = Square(10, 7, 6)

        self.assertEqual(str(r), f'[Square] ({r.id}) 7/6 - 10')

    def test_str_x_y_id(self):
        """Test the string representation with defined specific parameters
        """
        r = Square(23, 4, 10, 98)

        self.assertEqual(str(r), f'[Square] (98) 4/10 - 23')

    def test_update_no_argumemt(self):
        """Test the behaviour when no parameter is passed for update.
        """
        self.r.update()

        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 0/0 - 10')

    def test_update_id_valid(self):
        """Test id update with valid number
        """
        self.r.update(89)

        self.assertEqual(str(self.r), f'[Square] (89) 0/0 - 10')

    def test_update_id_str(self):
        """Test id update with string
        """
        self.r.update('four')

        self.assertEqual(str(self.r), f'[Square] (four) 0/0 - 10')

    def test_update_id_negative(self):
        """Test id update with value < 0
        """
        self.r.update(-5)

        self.assertEqual(str(self.r), f'[Square] (-5) 0/0 - 10')

    def test_update_id_float(self):
        """Test id update with float
        """
        self.r.update(6.6)

        self.assertEqual(str(self.r), f'[Square] (6.6) 0/0 - 10')

        self.r.update(-6.6)

        self.assertEqual(str(self.r), f'[Square] (-6.6) 0/0 - 10')

    def test_update_id_tuple(self):
        """Test id update with a tuple"""
        self.r.update((3, 4, 'five'))

        id = (3, 4, 'five')

        self.assertEqual(str(self.r), f'[Square] ({id}) 0/0 - 10')

    def test_update_id_dict(self):
        """Test id update with a dictionary
        """
        self.r.update({'name': 2, 'id': 78})

        id = {'name': 2, 'id': 78}
        self.assertEqual(str(self.r), (f"[Square] ({id}) 0/0 - 10"))

    def test_update_id_None(self):
        """Test id update with a None"""
        self.r.update(None)

        self.assertEqual(str(self.r), f'[Square] (None) 0/0 - 10')

    def test_update_width_valid(self):
        """Test that a valid width is updated properly"""
        self.r.update(89, 12)

        self.assertEqual(str(self.r), f'[Square] (89) 0/0 - 12')

    def test_update_width_None(self):
        """Test that an exception is raised when width is updated to None
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, None)

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_str(self):
        """Test that an exception is raised when width is updated with string
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, "four")

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_float(self):
        """Test that an exception is raised when width is updated with
        a float
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, -9.8)

        self.assertEqual(str(msg.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 9.8)

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_dict(self):
        """Test that an exception is raised when width is updated with
        a dictionary
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, {"width": 23})

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_tuple(self):
        """Test that an exception is raised when width is updated with
        a tuple
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, ("width", 23))

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_list(self):
        """Test that an exception is raised when width is updated with
        a list
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, ["size", 23])

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_negative(self):
        """Test that an exception is raised when width is updated with
        a value < 0
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(89, -6)

        self.assertEqual(str(msg.exception), 'width must be > 0')

    def test_update_width_zero(self):
        """Test that an exception is raised when width is updated with
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(89, 0)

        self.assertEqual(str(msg.exception), 'width must be > 0')

    def test_update_id_width_height_x_y_valid(self):
        """Test that a valid y is updated properly"""
        self.r.update(89, 6, 3, 2)

        self.assertEqual(str(self.r), f'[Square] (89) 3/2 - 6')

    def test_update_id_width_height_x_y_None(self):
        """Test that an exception is raised when y is updated to None
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, 3, None)

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_str(self):
        """Test that an exception is raised when y is updated with string
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 6, 3, "four")

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_float(self):
        """Test that an exception is raised when y is updated with
        a float
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, 3, -9.8)

        self.assertEqual(str(msg.exception), 'y must be an integer')

        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 6, 3, 9.8)

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_dict(self):
        """Test that an exception is raised when y is updated with
        a dictionary
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 6, 3, {"y": 23})

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_tuple(self):
        """Test that an exception is raised when y is updated with
        a tuple
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 6, 3, ("y", 23))

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_list(self):
        """Test that an exception is raised when y is updated with
        a list
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 6, 3, ["y", 23])

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_negative(self):
        """Test that an exception is raised when y is updated with
        a value < 0
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(89, 6, 3, -6)

        self.assertEqual(str(msg.exception), 'y must be >= 0')

    def test_update_id_width_height_x_y_zero(self):
        """Test that y is updated properly
        """
        self.r.update(89, 6, 3, 0)

        self.assertEqual(str(self.r), f'[Square] (89) 3/0 - 6')

    def test_update_id_width_height_x_valid(self):
        """Test that a valid y is updated properly"""
        self.r.update(89, 12, 3)

        self.assertEqual(str(self.r), f'[Square] (89) 3/0 - 12')

    def test_update_id_width_height_x_None(self):
        """Test that an exception is raised when x is updated to None
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, None)

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_str(self):
        """Test that an exception is raised when x is updated with string
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, "four")

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_float(self):
        """Test that an exception is raised when x is updated with
        a float
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, -9.8)

        self.assertEqual(str(msg.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, 9.8)

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_dict(self):
        """Test that an exception is raised when x is updated with
        a dictionary
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, {"x": 23})

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_tuple(self):
        """Test that an exception is raised when x is updated with
        a tuple
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, ("x", 23))

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_list(self):
        """Test that an exception is raised when x is updated with
        a list
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(89, 12, ["x", 23])

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_negative(self):
        """Test that an exception is raised when x is updated with
        a value < 0
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(89, 12, -6)

        self.assertEqual(str(msg.exception), 'x must be >= 0')

    def test_update_id_width_height_x_zero(self):
        """Test that x is updated properly
        """
        self.r.update(89, 12, 0)

        self.assertEqual(str(self.r), f'[Square] (89) 0/0 - 12')

    def test_update_all(self):
        """Test that all attributes are updated together properly
        """
        r = Square(10, 10, 10, 10)

        r.update(5, 3, 3, 1)

        self.assertEqual(str(r), f'[Square] (5) 3/1 - 3')

        r.update(25, 15, 9, 7)

        self.assertEqual(str(r), f'[Square] (25) 9/7 - 15')

    def test_update_over_arg(self):
        """Test that index error is prevented when there are
        more that specified instance attribute for update.
        """
        self.r.update(10, 6, 2, 1, 3)

        self.assertEqual(str(self.r), f'[Square] (10) 2/1 - 6')

    def test_update_None(self):
        """Test that id is None when passed as update
        """
        r = Square(10, id=3)
        r.update(None)

        self.assertEqual(str(r), f'[Square] (None) 0/0 - 10')

    def test_update_by_keyword(self):
        """Test that parameters are updated by specified keyword"""
        self.r.update(id=12, width=3, x=2, y=3)

        self.assertEqual(str(self.r), f'[Square] (12) 2/3 - 3')

    def test_update_valid_id_by_keyword(self):
        """Test that id is updated by keyword
        """
        self.r.update(id=8)

        self.assertEqual(str(self.r), f'[Square] (8) 0/0 - 10')

    def test_update_id_str_by_keyword(self):
        """Test id update with string
        """
        self.r.update(id='four')

        self.assertEqual(str(self.r), f'[Square] (four) 0/0 - 10')

    def test_update_id_negative_by_keyword(self):
        """Test id update with value < 0
        """
        self.r.update(id=-5)

        self.assertEqual(str(self.r), f'[Square] (-5) 0/0 - 10')

    def test_update_id_float_by_keyword(self):
        """Test id update with float
        """
        self.r.update(id=6.6)

        self.assertEqual(str(self.r), f'[Square] (6.6) 0/0 - 10')

        self.r.update(id=-6.6)

        self.assertEqual(str(self.r), f'[Square] (-6.6) 0/0 - 10')

    def test_update_id_tuple_by_keyword(self):
        """Test id update with a tuple"""
        self.r.update(id=(3, 'five'))

        id = (3, 'five')

        self.assertEqual(str(self.r), f'[Square] ({id}) 0/0 - 10')

    def test_update_id_dict_by_keyword(self):
        """Test id update with a dictionary
        """
        self.r.update(id={'name': 2, 'id': 78})

        id = {'name': 2, 'id': 78}
        self.assertEqual(str(self.r), (f"[Square] ({id}) 0/0 - 10"))

    def test_update_id_None_by_keyword(self):
        """Test id update with a None"""
        self.r.update(id=None)

        self.assertEqual(str(self.r), f'[Square] (None) 0/0 - 10')

    def test_update_width_valid_by_keyword(self):
        """Test that a valid width is updated properly"""
        self.r.update(id=89, size=12)

        self.assertEqual(str(self.r), f'[Square] (89) 0/0 - 12')

    def test_update_width_None_by_keyword(self):
        """Test that an exception is raised when width is updated to None
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size=None)

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_str_by_keyword(self):
        """Test that an exception is raised when width is updated with string
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size="four")

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_float_by_keyword(self):
        """Test that an exception is raised when width is updated with
        a float
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size=-9.8)

        self.assertEqual(str(msg.exception), 'width must be an integer')

        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size=9.8)

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_dict_by_keyword(self):
        """Test that an exception is raised when width is updated with
        a dictionary
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size={"width": 23})

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_tuple_by_keyword(self):
        """Test that an exception is raised when width is updated with
        a tuple
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size=("width", 23))

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_list_by_keyword(self):
        """Test that an exception is raised when width is updated with
        a list
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size=["width", 23])

        self.assertEqual(str(msg.exception), 'width must be an integer')

    def test_update_width_negative_by_keyword(self):
        """Test that an exception is raised when width is updated with
        a value < 0
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(id=89, size=-6)

        self.assertEqual(str(msg.exception), 'width must be > 0')

    def test_update_width_zero_by_keyword(self):
        """Test that an exception is raised when width is updated with
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(id=89, size=0)

        self.assertEqual(str(msg.exception), 'width must be > 0')

    def test_update_id_width_height_x_y_valid_by_keyword(self):
        """Test that a valid y is updated properly"""
        self.r.update(id=89, size=12, x=3, y=2)

        self.assertEqual(str(self.r), f'[Square] (89) 3/2 - 12')

    def test_update_id_width_height_x_y_None_by_keyword(self):
        """Test that an exception is raised when y is updated to None
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size=12, x=3, y=None)

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_str_by_keyword(self):
        """Test that an exception is raised when y is updated with string
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=3, y="four")

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_float_by_keyword(self):
        """Test that an exception is raised when y is updated with
        a float
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=3, y=-9.8)

        self.assertEqual(str(msg.exception), 'y must be an integer')

        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=3, y=9.8)

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_dict_by_keyword(self):
        """Test that an exception is raised when y is updated with
        a dictionary
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=3, y={"y": 23})

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_tuple_by_keyword(self):
        """Test that an exception is raised when y is updated with
        a tuple
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=3, y=("y", 23))

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_list_by_keyword(self):
        """Test that an exception is raised when y is updated with
        a list
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=3, y=["y", 23])

        self.assertEqual(str(msg.exception), 'y must be an integer')

    def test_update_id_width_height_x_y_negative_by_keyword(self):
        """Test that an exception is raised when y is updated with
        a value < 0
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(id=89, width=12, height=6, x=3, y=-6)

        self.assertEqual(str(msg.exception), 'y must be >= 0')

    def test_update_id_width_height_x_y_zero_by_keyword(self):
        """Test that y is updated properly
        """
        self.r.update(id=89, size=12, x=3, y=0)

        self.assertEqual(str(self.r), f'[Square] (89) 3/0 - 12')

    def test_update_id_width_height_x_valid_by_keyword(self):
        """Test that a valid y is updated properly"""
        self.r.update(id=89, size=12, x=3)

        self.assertEqual(str(self.r), f'[Square] (89) 3/0 - 12')

    def test_update_id_width_height_x_None_by_keyword(self):
        """Test that an exception is raised when x is updated to None
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, size=12, x=None)

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_str_by_keyword(self):
        """Test that an exception is raised when x is updated with string
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x="four")

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_float_by_keyword(self):
        """Test that an exception is raised when x is updated with
        a float
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=-9.8)

        self.assertEqual(str(msg.exception), 'x must be an integer')

        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=9.8)

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_dict_by_keyword(self):
        """Test that an exception is raised when x is updated with
        a dictionary
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x={"x": 23})

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_tuple_by_keyword(self):
        """Test that an exception is raised when x is updated with
        a tuple
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=("x", 23))

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_list_by_keyword(self):
        """Test that an exception is raised when x is updated with
        a list
        """
        with self.assertRaises(TypeError) as msg:
            self.r.update(id=89, width=12, height=6, x=["x", 23])

        self.assertEqual(str(msg.exception), 'x must be an integer')

    def test_update_id_width_height_x_negative_by_keyword(self):
        """Test that an exception is raised when x is updated with
        a value < 0
        """
        with self.assertRaises(ValueError) as msg:
            self.r.update(id=89, width=12, height=6, x=-6)

        self.assertEqual(str(msg.exception), 'x must be >= 0')

    def test_update_id_width_height_x_zero_by_keyword(self):
        """Test that x is updated properly
        """
        self.r.update(id=89, size=12, x=0)

        self.assertEqual(str(self.r), f'[Square] (89) 0/0 - 12')

    def test_update_by_keyword_combination(self):
        """Test update with keyword by random key value update
        """
        self.r.update(size=1)
        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 0/0 - 1')

        self.r.update(size=1, x=2)
        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 2/0 - 1')

        self.r.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(self.r), f'[Square] (89) 3/1 - 2')

        self.r.update(x=1, y=3, size=4)
        self.assertEqual(str(self.r), f'[Square] (89) 1/3 - 4')

    def test_invalid_keyword_mixture(self):
        """Test that invalud keyword not not affect the seeting of attributes
        """
        self.r.update(h=1)
        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 0/0 - 10')

        self.r.update(size=1, x=2, w=34)
        self.assertEqual(str(self.r), f'[Square] ({self.r.id}) 2/0 - 1')

        self.r.update(y=1, i=2, size=2, x=3, id=89)
        self.assertEqual(str(self.r), f'[Square] (89) 3/1 - 2')

        self.r.update(a=3, x=1, height=2, y=3, size=4, z=5)
        self.assertEqual(str(self.r), f'[Square] (89) 1/3 - 4')
