"""
Module Name: tests/test_models/test_base.py
Description: This module provide ``base`` class for testing
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


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

    def test_Rectangle_to_json_string(self):
        """Test that the list of dictionary is coverted to json string
        """
        r = Rectangle(2, 3, 1, 2, 5)

        json_dict = Base.to_json_string([r.to_dictionary()])

        self.assertEqual(
                json_dict,
                '[{"id": 5, "width": 2, "height": 3, "x": 1, "y": 2}]'
        )

    def test_Square_to_json_string(self):
        """Test that a list of square instance dictionary
        is coverted to json string
        """
        s = Square(6, id=10)

        json_dict = Base.to_json_string([s.to_dictionary()])

        self.assertEqual(
                json_dict,
                '[{"id": 10, "size": 6, "x": 0, "y": 0}]'
                )

    def test_to_json_string_no_input(self):
        """Test that empty list is returned
        """
        empty_list = Base.to_json_string(None)
        self.assertEqual(empty_list, '[]')

        empty_list = Base.to_json_string([])
        self.assertEqual(empty_list, '[]')

    def test_rectangle_save_to_file(self):
        """Test that the expected Rectangle instance data is saved to the file
        """
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])

        expected = ('[{"id": ' + f'{r.id}, ' +
                    '"width": 1, "height": 2, "x": 0, "y": 0}]')
        with open('Rectangle.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), expected)

        r = Rectangle(2, 3, 0, 1, 4)
        r2 = Rectangle(4, 6, 2, 3, 9)

        r_dict = '{"id": 4, "width": 2, "height": 3, "x": 0, "y": 1}'
        r2_dict = '{"id": 9, "width": 4, "height": 6, "x": 2, "y": 3}'

        expected = f'[{r_dict}, {r2_dict}]'

        Rectangle.save_to_file([r, r2])

        with open('Rectangle.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), expected)

    def test_Rectangle_save_to_file_None(self):
        """Test if an empty list is saved
        """
        Rectangle.save_to_file(None)

        with open('Rectangle.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_Rectangle_save_to_file_empty(self):
        """Test if an empty list is saved
        """
        Rectangle.save_to_file([])

        with open('Rectangle.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_Square_save_to_file(self):
        """Test that the expected Square instance data is saved to the file
        """
        s = Square(2, 1, 2, 7)
        s1 = Square(3, 4, 2, 1)
        s2 = Square(3, 4, 2, 8)

        s_dict = '{"id": 7, "size": 2, "x": 1, "y": 2}'
        s2_dict = '{"id": 1, "size": 3, "x": 4, "y": 2}'
        s3_dict = '{"id": 8, "size": 3, "x": 4, "y": 2}'

        expected = f'[{s_dict}, {s2_dict}, {s3_dict}]'

        Square.save_to_file([s, s1, s2])

        with open('Square.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), expected)

    def test_Square_save_to_file_None_empty(self):
        """Test if an empty list is saved
        """
        Square.save_to_file(None)

        with open('Square.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

        Square.save_to_file([])
        with open('Square.json', mode='r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')
            self.assertIsNotNone(f.read())

    def test_from_json_string(self):
        """Test that json string is deserialized
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]

        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)

        self.assertEqual(list_output, list_input)

    def test_from_json_string_no_input(self):
        """Test that empty list is returned
        """
        empty_list = Base.from_json_string(None)
        self.assertEqual(empty_list, [])

        empty_list = Base.from_json_string('[]')
        self.assertEqual(empty_list, [])

    def test_rectangle_create(self):
        """Test the creation of a rectangle instance from an attribute
        dictionary
        """
        r1 = Rectangle(3, 5, 1, id=9)
        r1_dictionary = r1.to_dictionary()

        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(str(r2), f'[Rectangle] (9) 1/0 - 3/5')

        self.assertNotEqual(r2, r1)

        self.assertIsNot(r2, r1)

    def test_square_create(self):
        """Test that the square instance is created from a dictionary
        of attributes
        """
        s1 = Square(2, 4, 1, 12)
        s1_dict = s1.to_dictionary()

        s2 = Square.create(**s1_dict)

        self.assertEqual(str(s2), f'[Square] (12) 4/1 - 2')

        self.assertNotEqual(s2, s1)

        self.assertIsNot(s2, s1)

    def test_rectangle_load_from_file(self):
        """Test that correct instances are loaded from file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        list_rect_input = [r1, r2]

        Rectangle.save_to_file(list_rect_input)

        list_rect_output = Rectangle.load_from_file()

        self.assertEqual(str(r1), str(list_rect_output[0]))
        self.assertEqual(str(r2), str(list_rect_output[1]))

    def test_rectangle_load_from_file_no_file(self):
        """Test that an empty list is return
        """
        try:
            os.remove('Rectangle.json')
        except FileNotFoundError:
            pass

        empty_list = Rectangle.load_from_file()

        self.assertEqual(empty_list, [])

    def test_square_load_from_file(self):
        """Test that expected data is loaded from file
        """
        s1 = Square(5)
        s2 = Square(7, 9, 1)

        list_square_input = [s1, s2]

        Square.save_to_file(list_square_input)

        list_square_output = Square.load_from_file()

        self.assertEqual(str(s1), str(list_square_output[0]))
        self.assertEqual(str(s2), str(list_square_output[1]))

    def test_square_load_from_file_no_file(self):
        """Test that an empty list is return
        """
        try:
            os.remove('Square.json')
        except FileNotFoundError:
            pass

        empty_list = Square.load_from_file()

        self.assertEqual(empty_list, [])
