#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys.
    """
    sorted_dict = sorted(a_dictionary.items())
    for x, y in sorted_dict:
        print("{}: {}".format(x, y))
