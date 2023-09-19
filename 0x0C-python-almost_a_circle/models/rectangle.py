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

    def __str__(self):
        """Overide str method.
        """
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}/{self.height}')

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
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        x and y is yet to be handled
        """
        print('\n' * self.y, end='')
        for h in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the object based on a variable
        number of arguments.

        This method allows updating one or more attributes
        of the object in a flexible way.

        Args:
            *args (int): Variable number of arguments.
                   1st argument (if provided) should be the id attribute
                   2nd argument (if provided) should be the width attribute
                   3rd argument (if provided) should be the height attribute
                   4th argument (if provided) should be the x attribute
                   5th argument (if provided) should be the y attribute

        Returns:
            None

        Example:
            # Create a rectangle instance
            r = Rectangle(10, 10, 10, 10, 20)

            # Update the parameters
            r.update(12, 3, 6, 5, 2)

            r.update(id=7, width=3, height=2, x=3, y=5)

        Note:
            Any attribute can be updated and all attributes may not be updated
            at once

        """
        if args:
            arg_name = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(arg_name):
                    setattr(self, arg_name[i], arg)
        elif kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
