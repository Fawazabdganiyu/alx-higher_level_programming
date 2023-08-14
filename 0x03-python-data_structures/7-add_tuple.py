#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples
    """
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    idx1 = tuple_a[0] + tuple_b[0]
    idx2 = tuple_a[1] + tuple_b[1]
    new_tuple = idx1, idx2
    return new_tuple
