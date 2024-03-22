#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            squared_item = item ** 2
            new_row.append(squared_item)
        square_matrix.append(new_row)
    return square_matrix