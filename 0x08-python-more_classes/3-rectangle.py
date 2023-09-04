#!/usr/bin/python3
"""
Module Name: 0-rectangle.py
Description: A module that provide ``Rectangle`` class
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


class Rectangle:
    """A class that defines a rectangle

    Attributes:
        with (int): Instance attribute for width of a rectangle
        height (int): Instance attribute for height of a rectangle

    """
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Width of a rectangle.

         Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero

        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: height of a rectangle

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero

        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """int: returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """int: returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """str: returns representation of rectangle with the character #.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for height in range(self.__height):
            rect.append('#' * self.__width)

        return "\n".join(rect)
