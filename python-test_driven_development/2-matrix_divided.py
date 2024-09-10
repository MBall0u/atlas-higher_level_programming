#!/usr/bin/python3
"""

This module divides the given matrix by the div provided.

"""


def matrix_divided(matrix, div):
    """

    a function that divides all elements of a matrix

    Args:
        matrix (int or float): a list of lists of integers or floats.
        div (int or float): the integer or float we are dividing each spot of the matrix by.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        TypeError: Each row of the matrix must have the same size.
        TypeError: div must be a number.
        ZeroDivisionError: division by zero.

    Returns:
        (list of lists) of int or float: a new matrix after each spot has been divided.
    """

    for row in matrix:
        for column in row:
            if not isinstance(column, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    new_matrix = []

    rows = len(matrix)
    columns = len(matrix[0])
    for row in matrix:
        if len(row) != columns:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(rows):
        new_matrix.append([0] * columns)

    for i in range(rows):
        for j in range(columns):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix