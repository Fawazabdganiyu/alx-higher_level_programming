#!/usr/bin/python3
"""
Module Name: 8-base_geometry.py
Description: This module provide ``BaseGeometry`` class
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        """Return str representation"""
        rect_class = str(self.__class__.__name__)
        rect_size = str(self.__size)
        return f"[{rect_class}] {rect_size}/{rect_size}"

    def area(self):
        """
        Returns Area of the square
        """
        return self.__size ** 2
