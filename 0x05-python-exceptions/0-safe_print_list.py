#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            count += 1
            print(item, end='')
        print()
        return count
    except TypeError:
        print("Invalid Format")
        pass
