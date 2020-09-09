#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    else:
        max = my_list[0]
        for m in my_list:
            if m > max:
                max = m
        return max
