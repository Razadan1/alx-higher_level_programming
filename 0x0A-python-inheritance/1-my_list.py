#!/usr/bin/python3
"""Defines an inherited class called LIST in MYList"""


class MyList(list):
    """Prints a sorted list in ascending order"""

    def print_sorted(self):
        listed = sorted(self)
        print(listed)
