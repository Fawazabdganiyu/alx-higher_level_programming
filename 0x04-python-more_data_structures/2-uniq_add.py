#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer).
    """
    my_list = set(my_list)
    adds = 0
    for x in my_list:
        adds += x
    return adds
