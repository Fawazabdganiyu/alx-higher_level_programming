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

        Raises:
            TypeError: If `size` is not an integer
            ValueError: If `size` is less than zero

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """int: A current size of a square

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than zero

        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for height in range(self.__size):
                for width in range(self.__size):
                    print("#", end="")
                print()
