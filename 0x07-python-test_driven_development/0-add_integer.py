#!/usr/bin/python3
""" A function that adds two integers"""


def add_integer(a, b=98):
    """ Adds two integers"""
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
