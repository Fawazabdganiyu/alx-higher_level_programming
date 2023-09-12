#!/usr/bin/python3
"""
Module Name: 0-read_file.py
Description: This module provide ``read_file`` function.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): The file to be read and printed

    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
