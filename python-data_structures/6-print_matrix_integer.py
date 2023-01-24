#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elem in matrix:
            i = 1
            length = len(elem)
            for elements in elem:
                if i == length:
                    print('{:d}'.format(elements), end='')
                else:
                    print('{:d}'.format(elements), end=' ')
                i += 1
            print()
