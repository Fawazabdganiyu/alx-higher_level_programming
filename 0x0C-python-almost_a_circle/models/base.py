#!/usr/bin/python3
"""
Module Name: models/base.py
Description: This module provides ``Base`` class.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


class Base:
    """A simple ``Base`` class definition

    Args:
        id (int): Identification

    Attributes:
        nb_objects (int): A private class attribute

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """A simple class constructor.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
