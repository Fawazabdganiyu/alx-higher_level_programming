#!/usr/bin/python3
"""
Module Name: 3-say_my_name.py
Description: This module provide a function ``say_my_name`` that prints
            My name is <first name> <last name>
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>

    Args:
        first_name (str): First name of the user
        last_name (str): Last name of the user

    Raises:
        TypeError: If any of ``first_name`` or ``last_name`` is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
