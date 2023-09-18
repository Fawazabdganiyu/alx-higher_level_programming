#!/usr/bin/python3
"""
Module Name: models/square.py
Description: This module defines ``Square`` class.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A definition of ``Square`` class inherited from Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor for square instance

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The identification of the square.

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The overloading __str__ method"""
        return (f'[Square] ({self.id}) {super().x}/{super().y} - '
                f'{super().width}')

    @property
    def size(self):
        """get/set size of the square

        Args:
            value (int): The value to set the size to.

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0

        Returns:
            int: The size of the square (both width and height).

        """
        return super().width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """pdate the attributes of the object based on a variable number of
        arguments and key-value pairs.

        This method allows updating one or more attributes of the object
        in a flexible way using both positional arguments (*args) and
        keyword arguments (**kwargs).

        Args:
            *args (int): Variable number of positional arguments
                   in the order of id, size, x, y.

            **kwargs (str: int): Variable keyword argument for named
                                 attribute update.

        Return:
            None

        """
        if args:
            args_name = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(args_name):
                    setattr(self, args_name[i], arg)
        elif kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)
