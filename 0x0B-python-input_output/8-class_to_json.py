#!/usr/bin/python3
"""
Module NAme: 8-class_to_json.py
Decription: This module provides ``class_to_json`` function
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def class_to_json(obj):
    """gives the dictionary description with simple data structure

    This function returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj (obj): an instance of a class

    Return: the dictionary description with simple data structure

    """
    return obj.__dict__
