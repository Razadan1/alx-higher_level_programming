#!/usr/bin/python3
""" A function that adds two integers"""


def add_integer(a, b=98):
    """ Adds two integers"""
    if isinstance(a, (float, int)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (float, int)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return int(a + b)
