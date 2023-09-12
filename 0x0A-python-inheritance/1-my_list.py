#!/usr/bin/python3
"""
Module Name: 1-my_list.py
Description: This module provide ``MyList`` class
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""

class MyList(list):
    """
    This is a `list` Derieved class for sorting

    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
