#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        lenx1 = len(matrix)
        lenx2 = len(matrix[0])
        for i in range(lenx1):
            for a in range(lenx2):
                if a == lenx2 - 1:
                    print(matrix[i][a])
                else:
                    print(matrix[i][a], end=' ')
    else:
        print()
