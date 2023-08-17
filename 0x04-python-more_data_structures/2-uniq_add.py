#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer).
    """
    from functools import reduce
    my_list = set(my_list)
    adds = reduce(lambda a, b: a + b, my_list)
    return adds
