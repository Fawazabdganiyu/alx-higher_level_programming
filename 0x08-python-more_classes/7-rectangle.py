#!/usr/bin/python3
"""
Module Name: 7-rectangle.py
Description: A module that provide ``Rectangle`` class
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


class Rectangle:
    """
    A class that defines a rectangle

    Attributes:
        with (int): Instance attribute for width of a rectangle
        height (int): Instance attribute for height of a rectangle
        number_of_instances (int): Class attribute to keep track
                    of number of instances created.
        print_symbol (str): Used as symbol for string representation

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialises a Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0)
            height (int): The height of the rectangle (default is 0)

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        int: The width of the rectangle.

         Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than zero

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
        """
        Calculate the area of the rectangle.

        Return:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Return:
            int: The perimeter of the rectangle

        """
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
            rect.append(str(self.print_symbol) * self.__width)

        return "\n".join(rect)

    def __repr__(self):
        """return a string representation of the rectangle.

        This is to be able to recreate a new instance by using eval().

        """
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        """
        Delete an instance

        Prints "Bye rectangle... "(... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted

        """
        print("Bye rectangle...")

        type(self).number_of_instances -= 1
