#!/bin/bash
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        for list in my_list[::-1]:
            print("{:d}".format(list))
