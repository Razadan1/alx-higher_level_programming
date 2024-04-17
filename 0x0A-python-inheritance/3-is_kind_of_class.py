#!/usr/bin/python3
""" A function that returns true if the object is an instance
of, or the object is an instance of a class that is inherited from"""


def is_kind_of_class(obj, a_class):
    """ Check if the its an instance of an inherited class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
