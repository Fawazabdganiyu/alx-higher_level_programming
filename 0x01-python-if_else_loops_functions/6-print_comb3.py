#!/usr/bin/python3
"""prints all possible different combinations of two digits."""
for x in range(9):
    for y in range(x + 1, 10):
        if x == 8 and y == 9:
            print("{:d}".format(89))
            continue
        print("{:d}".format(x), end='')
        print("{:d}".format(y), end=', ')
