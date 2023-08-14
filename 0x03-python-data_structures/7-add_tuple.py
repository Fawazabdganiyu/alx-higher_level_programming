#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples
    """
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        idx1 = tuple_a[0] + tuple_b[0]
        idx2 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) >= 2 and len(tuple_b) == 0:
        idx1 = tuple_a[0]
        idx2 = tuple_a[1]
    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        idx1 = tuple_a[0] + tuple_b[0]
        idx2 = tuple_a[1]
    elif len(tuple_a) == 0 and len(tuple_b) >= 2:
        idx1 = tuple_b[0]
        idx2 = tuple_b[0]
    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
        idx1 = tuple_a[0] + tuple_b[0]
        idx2 = tuple_b[1]
    elif len(tuple_a) == 0 and len(tuple_b) == 0:
        idx1 = 0
        idx2 = 0
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        idx1 = tuple_a[0]
        idx2 = tuple_b[0]
    new_tuple = idx1, idx2
    return new_tuple
