#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = (0, 0)
    tuple_1 = tuple_a + new_tuple
    tuple_2 = tuple_b + new_tuple
    new_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return new_tuple
