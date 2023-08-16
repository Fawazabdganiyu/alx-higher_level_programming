#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list.
    """
    new_list = my_list[:]
    for x in range(len(my_list)):
        if new_list[x] == search:
            new_list[x] = replace

            print(new_list[x])
    return new_list
