#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_tuple_a = tuple_a + (0, 0)
    first_tuple_b = tuple_b + (0, 0)
    sum_tuple_a = (first_tuple_a[0] + first_tuple_b[0])
    sum_tuple_b = (first_tuple_a[1] + first_tuple_b[1])
    tuple_results = (sum_tuple_a, sum_tuple_b)
    return (tuple_results)