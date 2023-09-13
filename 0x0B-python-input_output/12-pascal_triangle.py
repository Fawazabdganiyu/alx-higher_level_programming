#!/usr/bin/python3
"""Module Name: 12-pascal_triangle.py
Description: This module provides ``pascal_triangle`` function
Author: FAwaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal's triangle of n

    Arg:
        n (int):

    Return:
        returns a list of lists of integers representing
        the Pascal's triangle of n

    """
    if n <= 0:
        return []

    return [1]
