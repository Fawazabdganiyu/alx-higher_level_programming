#!/usr/bin/python3
"""
Module Name: 101-add_attribute.py
Description: This module provides ``add_attribute`` function.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def add_attribute(obj, attr_name, attr_value):
    """adds a new attribute to an object if it's possible

    Args:
        obj (obj): The object to which new attribute would be added.
        attr_name (str): The name of the new attribute
        attr_value (obj): The corresponding value of the new attribute

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
