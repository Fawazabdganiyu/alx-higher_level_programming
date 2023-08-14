#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers.
    """
    for row in matrix:
        i = 0
        for column in row:
            print("{:d}".format(column), end='')
            i += 1
            if i < len(row):
                print(end=' ')
        print()
