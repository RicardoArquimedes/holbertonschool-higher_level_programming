#!/usr/bin/python3

# Write a function that replaces an element in a list at
# a specific position without modifying the original list


def new_in_list(my_list, idx, element):
    if idx == -1:
        return my_list.copy()
    if idx > len(my_list) - 1:
        return my_list.copy()
    for new in range(len(my_list)):
        if idx == new:
            new_list = my_list.copy()
            new_list[new] = element
            return new_list
