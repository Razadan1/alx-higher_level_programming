#!/usr/bin/python3
""" This function appends a srting or words to a file"""


def append_write(filename="", text=""):
    """ Appends string to a file """
    with open(filename, mode="a", encoding="utf-8") as appendFile:
        chars_added = appendFile.write(text)
    return chars_added