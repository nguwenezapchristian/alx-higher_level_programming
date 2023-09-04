#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ divide all element of matrix and return new matrix
    Args:
        matrix([[]]): a matrix
        div(int): a divisor
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be an integer or a float")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            divided = round(element / div, 2)
            new_row.append(divided)
        new_matrix.append(new_row)
    return new_matrix
