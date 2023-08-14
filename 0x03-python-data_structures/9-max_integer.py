#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list.
    """
    my_list_len = len(my_list)
    if my_list_len == 0:
        return None

    my_list.sort()
    max_value = my_list[my_list_len - 1]
    return max_value
