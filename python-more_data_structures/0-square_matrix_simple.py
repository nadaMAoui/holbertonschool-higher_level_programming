#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if len(matrix) > 0:
        for elements in matrix:
            new_matrix.append(list(map(lambda a: a**2, elements)))
        return new_matrix
