#!/usr/bin/python3
"""creates a copy of the string, removing the character at the position n"""


def remove_char_at(str, n):
    new_str = ''
    for x in range(len(str)):
        if x != n:
            new_str += str[x]
    return new_str
