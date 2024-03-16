#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for col in row:
                if col != row[-1]:
                    print("{:d}".format(col), end=" ")
                else:
                    print("{:d}".format(col), end="")
            print()
