#!/usr/bin/python3
"""prints numbers from 0 to 99"""
for num in range(100):
    if num < 99:
        print("{:02d}".format(num),  end=', ')
        continue
    else:
        print("{:d}".format(num))
