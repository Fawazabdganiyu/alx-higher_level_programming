#!/usr/bin/python3
"""Square class definition"""


class Square:
    """defines a square

    Attributes:
        __size: Size of a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialises the instance attributes

        Args:
            size (int): The size of the square
            positon (int): Position of the square

        Raises:
            TypeError: If `size` is not an integer or `position` is not a tuple
                of 2 positive integers
            ValueError: If `size` is less than zero

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = position
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            return

        if self.__position and self.__position[1] > 0:
            print('\n' * self.__position[1], end="")

        for height in range(self.__size):
            if self.__position and self.__position[0] > 0:
                print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """tuple(int, int): Position of the square

        Raises:
            TypeError: If position is not a tuple of 2 of positive integers

        """
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(val, int) and val >= 0 for val in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
