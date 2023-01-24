#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elements in matrix:
            length = len(elements)
        for i in range(length):
            for j in range(length):
                if (j + 1):
                    print("{:d}".format(matrix[i][j]), end=" "if (j % 3) else "\n")
                else:
                    print()