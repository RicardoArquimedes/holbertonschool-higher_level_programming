#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for val in range(len(row)):
            if val is len(row) - 1:
                print('{:d}'.format(row[val]), end="")
            else:
                print('{:d} '.format(row[val]), end="")
        print()
