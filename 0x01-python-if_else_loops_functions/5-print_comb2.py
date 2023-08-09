#!/usr/bin/python3
"""prints numbers from 0 to 99"""
for num in range(100):
    if num < 10:
        print("{:d}{:d}".format(0, num),  end=', ')
        continue
    elif num < 99:
        print("{:d}".format(num), end=', ')
    else:
        print("{:d}".format(num))
