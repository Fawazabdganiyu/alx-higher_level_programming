#!/usr/bin/python3
"""
Module Name: 0-lookup.py
Description: This module provide ``lookup`` function
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def lookup(obj):
    """
    returns the list of available attributes
    and methods of an object

    Args:
        obj (obj): The object to lookup its attributes and methods.

    Return: A list object

    """
    return dir(obj)
