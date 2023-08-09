#!/usr/bin/python3
"""prints a string in uppercase followed by a new line."""


def uppercase(str):
    for ch in str:
        print("{}".format(chr(ord(ch) - 32) if ord(ch) >= 97
              and ord(ch) <= 122 else ch), end='')
    print()
