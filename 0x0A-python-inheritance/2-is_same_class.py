#!/usr/bin/python3
""" A function that returns true if the objects is exactly
the same of the class"""


def is_same_class(obj, a_class):
    """ returns true if it is the same as a_class"""
    return type(obj) is a_class
