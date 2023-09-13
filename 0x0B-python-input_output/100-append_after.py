#!/usr/bin/python3
"""Module Name: 100-append_after.py
Description: This module provides ``append_after`` function
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (str): The filename
        search_string (str): The string to append after.
        new_string (str): THe string to be appended.

    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
