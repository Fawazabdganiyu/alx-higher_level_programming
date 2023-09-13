#!/usr/bin/python3
"""
Module Name: 8-base_geometry.py
Description: This module provide ``BaseGeometry`` class
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
