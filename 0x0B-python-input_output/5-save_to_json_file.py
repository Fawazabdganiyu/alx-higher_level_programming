#!/usr/bin/python3
"""
Module Name: 5-save_to_json_file.py
Description: THis module provides ``save_to_json_file`` function
Author: FAwaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (obj): The Object to be written
        filename (str): A file to write to

    """
    import json

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
