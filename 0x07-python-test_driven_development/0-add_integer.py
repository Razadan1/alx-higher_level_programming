#!/usr/bin/python3
""" A function that adds two integers"""


def add_integer(a, b=98):
    """ Adds two integers"""
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return int(a + b)
