#!/bin/bash

# Write a function that print an integer in reverse


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        for list in reversed(my_list):
            print(list)
