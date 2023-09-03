#!/usr/bin/python3
"""
Module Name: 2-matrix_divided.py
Description: This module provide ``matrix_divided`` function to divide all
elements of a matrix.
Author: Fawaz Abdganiyu <fawazabdganiyu@gmail.com>
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix (list of lists): a list of lists of integers or floats
        div (int, float): a number (integer or float) to divide with

    Raises:
        TypeError: If `matrix` is not a list of lists of integers or floats.
            If each row of `matrix` are not of the same size.
            If `div` is not a number(integer or float).
        ZeroDivisionError: If `div` is equal to zero.

    Return: A new matrix with result of division of `matrix` by `div`

    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float)) for row in matrix
                    for elem in row) or
            matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix.copy()]
