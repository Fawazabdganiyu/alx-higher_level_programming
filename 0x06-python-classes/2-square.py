#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Initialises the instance attributes

        Args:
            size: The size of the square
        """
        try:
            if isinstance(size, int) and size >= 0:
                self.__size = size
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
