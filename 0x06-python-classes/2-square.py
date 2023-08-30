#!/usr/bin/python3
"""Square class definition"""


class Square:
    """defines a square

    Attributes:
        __size: Size a square
    """
    def __init__(self, size=0):
        """Initialises the instance attributes with validation

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
