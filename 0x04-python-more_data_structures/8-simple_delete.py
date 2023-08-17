#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """deletes a key in a dictionary.
    """
    if key in a_dictionary:
        a_dictionary.pop(key)
    return a_dictionary
