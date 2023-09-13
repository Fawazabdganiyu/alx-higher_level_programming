#!/usr/bin/python3
"""
Module Name: 100-my_int.py
Description: This module provides ``MyInt`` class.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


class MyInt(int):
    """Custom "int" class that inverts '==' and '!=' operators
    """
    def __eq__(self, value):
        """Overides equal method"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Overides not equal method"""
        return super().__eq__(value)
