#!/usr/bin/python3
"""
Module Name: 7-base_geometry.py
Description: This module provide ``BaseGeometry`` class
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


class BaseGeometry:
    """
    A simple ``BaseGeometry`` class
    """
    def area(self):
        """
        Not implemented but raises an exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates an integer

        Args:
            name (str): The name of the argument
            value (int): The argument to be validated.

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or greater than zero
        """
        if type(value) != int:
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            raise ValueError(f"{value} must be greater than 0")
