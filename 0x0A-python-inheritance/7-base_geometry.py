#!/usr/bin/python3
""" A class based on task 6"""


class BaseGeometry:
    """ A class based on task 6"""
    def area(self):
        """ Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
