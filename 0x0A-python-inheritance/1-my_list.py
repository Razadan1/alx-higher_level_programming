#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        listed = sorted(self)
        print(listed)
