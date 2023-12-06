#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = matrix.copy()
    size = len(matrix)
    for i in range(size):
        matrix2[i] = list(map(lambda x: x**2, matrix[i]))
    return (matrix2)
