#!/usr/bin/python3
"""Square class definition"""


class Square:
    """defines a square

    Attributes:
        __size: Size of a square
    """
    def __init__(self, size=0):
        """Initialises the instance attributes

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        return int(self.__size) ** 2
