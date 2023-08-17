#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value.
    """
    if a_dictionary is None or not a_dictionary:
        return None
    best_score = 0
    for key, value in a_dictionary.items():
        if value >= best_score:
            best_score = value
            best_key = key
    return best_key
