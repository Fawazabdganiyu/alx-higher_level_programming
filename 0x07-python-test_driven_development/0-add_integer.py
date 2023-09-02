#!/usr/bin/python3
"""
Module Name: 0-add_integer.py
Description: This module provide a ``add_integer`` function to add two integers
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>
"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args:
        a (int, float): First Operand
        b (int, float): Second optional operand

    Raises:
        TypeError: If any argumnet is not an integer or float

    Return: a + b casted to int if in float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
