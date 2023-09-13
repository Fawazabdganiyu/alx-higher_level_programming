#!/usr/bin/python3
"""
Module Name: 6-load_from_json_file.py
Description: This module provides ``load_from_json_file`` function
Author: Fawaz Abdagniyu <fawazabdganiyu@gmail.com>

"""


def load_from_json_file(filename):
    """creates an Object from a "JSON file"

    Arg:
        filename (str): The filename to read from.

    """
    import json

    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
