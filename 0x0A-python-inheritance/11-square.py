#!/usr/bin/python3
"""
Module Name: 8-base_geometry.py
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


class Rectangle(BaseGeometry):
    """A representation of Rectangle class
    """
    def __init__(self, width, height):
        """instantiation

        Args:
            width (int): The width of the geometry
            height (int): The height of the geometry

        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Returns ``str`` representation of the rectangle
        """
        rect_class = str(self.__class__.__name__)
        rect_width = str(self.__width)
        rect_height = str(self.__height)
        return f"[{rect_class}] {rect_width}/{rect_height}"

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """A representation of Square"""
    def __init__(self, size):
        """Instantiation

        Args:
            size (int): The size of the square

        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns Area of the square
        """
        return self.__size ** 2
