#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the length of a string and its first character.
    """
    length = len(sentence)
    str_0 = sentence[0] if length != 0 else None
    tuple_pack = length, str_0
    return tuple_pack
