#!/usr/bin/python3
"""
Module Name: 3-to_json_string.py
Description: This module provides ``to_json_string`` function.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj (obj): The objectec to be converted to json.

    Return:
        The JSON representation of the object (string)

    """
    import json

    return json.dumps(my_obj)
