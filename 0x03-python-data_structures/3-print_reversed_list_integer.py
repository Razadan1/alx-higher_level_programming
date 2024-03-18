#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_lst = my_list[::-1]
    for item in reversed_lst:
        print("{:d}".format(item))
