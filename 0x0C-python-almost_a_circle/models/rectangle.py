#!/usr/bin/python3
"""
Module Name: models/rectangle.py
Description: This module provides ``Rectangle`` class.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class definition

    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int):
        y (int):

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        x (int): The position of the rectangle in x direction
        y (int): The position of the rectangle in y direction

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiations
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets and sets width of the rectangle

        Args:
            value (int): The value to set the width to
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets and sets the height of the rectangle.

        Args:
            value (int): The value to set the height to

        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets and sets x position of the rectangle

        Args:
            value (int): The value to set x to

        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets and sets y position of the rectangle

        Args:
            value (int): The y position to set the rectangle to.

        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        x and y is yet to be handled
        """
        for h in range(self.__height):
            print('#' * self.__width)
