#!/usr/bin/python3
"""
Module Name: 5-text_indentation.py
Description: This module provide a ``text_indentation`` function.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text (str): Text to be formated

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        if char in '.?:':
            new_text += char
            new_text += '\n' * 2
        elif char == ' ' and new_text and new_text[-1] == '\n':
            pass
        else:
            new_text += char
    print(new_text.strip(" "), end="")
