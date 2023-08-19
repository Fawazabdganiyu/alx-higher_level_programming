#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order.
    """
    if my_list is not None:
        my_list.reverse()
        for elem in my_list:
            print("{:d}".format(elem))
