#!/usr/bin/python3
"""
Module Name: 6-peak.py
Description: Provide a `find_peak` function
"""


def find_peak(list_of_integers):
    """Find the largest number in a list of unsorted integers
    """
    int_list = list_of_integers[:]
    peak = None
    if int_list != []:
        peak = max(int_list)

    return peak
