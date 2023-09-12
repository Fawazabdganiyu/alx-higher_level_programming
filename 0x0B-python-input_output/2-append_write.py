#!/usr/bin/python3
"""
Module Name: 2-append_write.py
Description: This module provide ``append_write`` function.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (str): The file to append to.
        text (str): The string to be appended.

    Return:
        The number of characters added.

    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
