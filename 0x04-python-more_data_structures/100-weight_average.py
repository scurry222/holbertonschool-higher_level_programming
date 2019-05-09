#!/usr/bin/python3
def weight_average(my_list=[]):
    n = sum([num[0] * num[1] for num in my_list])
    result = n / sum([num[1] for num in my_list])
    if my_list:
        return result
    else:
        return 0
