#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            col = len(row)
            for i in range(col):
                if i == col -1:
                    print("{:d}".format(row[i]), end="\n")
                else:
                    print("{:d}".format(row[i]), end=" ")
    else:
        print()
