#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    if matrix:
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                squared.append(pow(matrix[row][col], 2))
    return squared
