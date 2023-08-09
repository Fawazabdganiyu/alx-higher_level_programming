#!/usr/bin/python3
"""prints a string in uppercase followed by a new line."""


def uppercase(str):
    case = ''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            case += chr(ord(ch) - 32)
        else:
            case += ch
    print("{}".format(case))
