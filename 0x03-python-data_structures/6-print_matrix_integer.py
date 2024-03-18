#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        if len(item) >= 3:
            print("{:d} {:d} {:d}".format(item[0], item[1], item[2]))
