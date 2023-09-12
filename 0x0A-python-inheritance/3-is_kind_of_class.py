#!/usr/bin/python3
"""
Module Name: 3-is_kind_of_class.py
Description: This module provide ``is_kind_of_class`` function
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def is_kind_of_class(obj, a_class):
    """
    confirms if isinstance of a class

    Args:
        obj (obj): The object to confirm its class
        a_class (class): The class to confirm if an object is exactly its
        instance.

    Return: True if the objext is an instance of the specified class,
    otherwise False.

    """
    return isinstance(obj, a_class)
