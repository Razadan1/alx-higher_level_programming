#!/usr/bin/python3
""" A function that returns true if the object is an instance of
a class that inherited from the specified class"""


def inherits_from(obj, a_class):
    """ Returns true if inherited an instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
