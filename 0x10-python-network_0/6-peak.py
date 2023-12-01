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
    if len(int_list) == 2:
        if int_list[0] > int_list[1]:
            peak = int_list[0]
        else:
            peak = int_list[1]

    if len(int_list) > 2:
        peak = 0
        i = 1
        try:
            while int_list[i]:
                if peak < int_list[i]:
                    if int_list[i - 1] >= int_list[i]:
                        peak = int_list[i - 1]
                    if int_list[i + 1] >= int_list[i]:
                        peak = int_list[i + 1]
                    if (int_list[i] > int_list[i - 1] and
                            int_list[i] > int_list[i + 1]):
                        peak = int_list[i]
                i += 2
        except IndexError:
            pass
    return peak
