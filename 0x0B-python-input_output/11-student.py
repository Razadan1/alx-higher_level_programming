#!/usr/bin/python3
""" A Class that defines a student based on Task 9"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ The main function for instanciating the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Checks if attrs is a list of strings """
        if attrs is not None and all(isinstance(i, str) for i in attrs):
            x = {}
            for a, b in self.__dict__.items():
                if a in attrs:
                    x[a] = b
            return x
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
