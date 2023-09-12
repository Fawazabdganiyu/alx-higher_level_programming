#!/usr/bin/python3
"""
Module Name: 4-inherits_from.py
Description: This module provide ``inherits_from`` function
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def inherits_from(obj, a_class):
    """
    confirms if "obj" is an inherited instance of "a_class"

    Args:
        obj (obj): The object to confirm its class
        a_class (class): The class to confirm if an object is exactly its
        instance.

    Return: True if the object is an instance of a class inherited (directly or
    indirectly) from the specified class,
    otherwise False.

    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
