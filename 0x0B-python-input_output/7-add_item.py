#!/usr/bin/python3
"""
Module Name: 7-add_item.py
Description: This module provides a script.
The script adds all arguments to a Python list, and then save them to a file
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_argument_to_list(args, filename):
    """adds all arguments to a Python list and save them to a file

    Args:
        args (list): Arguments to be added to a list
        filename (str): The file to save to.

    """
    # Check if file exists; if not, an empty list is created
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(args)

    # Save the updated Python list to the file
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    args = argv[1:]  # Args will be an empty list if argument count < 2

    # Call the above function to add the args to the list and save
    add_argument_to_list(args, "add_item.json")
