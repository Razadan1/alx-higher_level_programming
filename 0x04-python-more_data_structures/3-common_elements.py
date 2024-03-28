#!/usr/bin/python3
def common_elements(set_1, set_2):
    for item in set_1:
       for item_2 in set_2:
            if item == item_2:
                return [item]
