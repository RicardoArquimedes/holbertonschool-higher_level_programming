#!/usr/bin/python3

# Write a function that replaces an element of a list at a specific position


def replace_in_list(my_list, idx, element):
    if idx == -1:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    for list in range(len(my_list)):
        if list == idx:
            my_list[list] = element
            return my_list
