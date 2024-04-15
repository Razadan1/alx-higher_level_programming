#!/usr/bin/python3
""" A function to list all available attributes"""
def lookup(obj):
    """ Returns the Attributes in the parent class Obj"""
    return dir(obj)
