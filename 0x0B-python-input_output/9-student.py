#!/usr/bin/python3
""" This function defines a student bypublic attributes"""



class Student:
    def __init__(self, first_name, last_name, age):
        """ The main function for instanciating the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This returns the dict format  of the object"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
