#!/usr/bin/python3
"""
Module Name: 101-nqueens.py
Description: This is a module for N queens puzzle
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>

"""
from sys import argv, exit


def nqueens():
    """
    prints every possible solution to the problem

    """


if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 1:
        print("Usage: nqueens N")
        exit(1)

    N = argv[1]

    if not N.isdigit():
        print("N must be a number")
        exit(1)
    if int(N) < 4:
        print("N must be at least 4")
        exit(1)
