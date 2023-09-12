#!/usr/bin/python3
"""
Module Name: 4-from_json_string.py
Description: This module provides ``from_json_string`` function.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string:

    Args:
        my_obj (obj): The objectec to be converted to json.

    Return:
        An object representation of a JSON string

    """
    import json

    return json.loads(my_str)
