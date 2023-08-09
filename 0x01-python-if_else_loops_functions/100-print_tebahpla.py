#!/usr/bin/python3
"""prints the ASCII alphabet, in reverse order, alternating lowercase
and uppercase (z in lowercase and Y in uppercase),
not followed by a new line
"""
ch = 122
while (ch >= 97):
    print("{}".format(chr(ch - 32) if ch % 2 != 0 else chr(ch)), end='')
    ch -= 1
