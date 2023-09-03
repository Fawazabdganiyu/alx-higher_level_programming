#!/usr/bin/python3
"""
Module Name: 4-print_square.py
Description: This module prints a square with the character #.
Author: Fawaz Abdagniyu <fawazabdganiyu@gmail.com>

"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): The size of the square to be printed with '#'.

    Raises:
        TypeError: If size is not an integer
                   If size is float and less than zero.
        ValueError: If size is less than zero.

    """
    if (type(size) is float and size < 0) or type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for height in range(size):
        print("#" * size)
