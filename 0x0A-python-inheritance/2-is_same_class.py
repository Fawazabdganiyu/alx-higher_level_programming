#!/usr/bin/python3
"""
Module Name: 2-is_same_class.py
Description: This module provide ``is_same_class`` function
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def is_same_class(obj, a_class):
    """
    confirms if "obj" is exactly of type "a_class"

    Args:
        obj (obj): The object to confirm its class
        a_class (class): The class to confirm if an object is exactly its
        instance.

    Return: True if the objext is exactly an instance of the specified class,
    otherwise False.

    """
    return type(obj) == a_class
