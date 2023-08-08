#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase,
not followed by a new line, except q and e
"""
character = 97
while character <= 122:
    if chr(character) == 'q' or chr(character) == 'e':
        character += 1
        continue
    print("{}".format(chr(character)), sep='', end='')
    character += 1
