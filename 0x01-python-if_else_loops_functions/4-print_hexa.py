#!/usr/bin/python3
"""prints all numbers from 0 to 98
in decimal and in hexadecimal
"""
for number in range(0, 99):
    print("{:d} = {}".format(number, hex(number)))
