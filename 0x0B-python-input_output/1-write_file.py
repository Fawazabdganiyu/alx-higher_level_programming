#!/usr/bin/python3
"""
Module Name: 1-write_file.py
Description: THis module provides ``write_file`` function.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and return
    the number of characters written

    Args:
        filename (str): The name of the file to be written to.
        text (str): The string to be written.

    Return: The number of characters written.

    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
