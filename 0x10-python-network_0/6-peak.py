#!/usr/bin/python3
"""
Module Name: 6-peak.py
Description: Provide a `find_peak` function
"""


def find_peak(list_of_integers):
    """Find the largest number in a list of unsorted integers
    """
    int_list = list_of_integers[:]
    if int_list == []:
        return None

    peak = 0
    last = len(int_list) - 1
    while peak < last:
        mid = (peak + last) // 2
        if int_list[mid] < int_list[mid + 1]:
            peak = mid + 1
        else:
            last = mid

    return int_list[peak]
