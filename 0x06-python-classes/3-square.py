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
        try:
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        return int(self.__size) ** 2
