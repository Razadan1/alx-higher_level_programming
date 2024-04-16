#!/usr/bin/python3
""" A function that reads files """


def read_file(filename=""):
    """ This function reads anyfile """
    with open(filename, encoding="utf-8") as readfile:
        print(readfile.read(), end="")
