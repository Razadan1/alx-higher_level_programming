#!/usr/bin/python3
""" This function writes to a file """


def write_file(filename="", text=""):
    """ This writes to a file"""
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        chars_written = writeFile.write(text)
    return chars_written
