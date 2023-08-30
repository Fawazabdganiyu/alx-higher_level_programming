#!/usr/bin/python3
class Square:
    """defines a square"""
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
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    @property
    def area(self):
        """returns the current square area"""
        if self.__size:
            a = self.__size
            return a
