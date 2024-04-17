#!/usr/bin/python3
""" A function that returns a list of integers in pascal triangle"""


def pascal_triangle(n):
    """print pascal"""
    p_triangle = [[0]*i for i in range(1, n+1)]
    for i in range(n):
        p_triangle[i][0] = 1
        p_triangle[i][-1] = 1
        for j in range(0, i//2):
            p_triangle[i][j+1] = p_triangle[i-1][j] + p_triangle[i-1][j+1]
            p_triangle[i][i-j-1] = p_triangle[i-1][j] + p_triangle[i-1][j+1]

    return p_triangle
