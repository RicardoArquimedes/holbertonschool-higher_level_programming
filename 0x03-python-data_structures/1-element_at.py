#!/usr/bin/python3

# Write a function that retrieves an element from a list


def element_at(my_list, idx):
    if idx == -1:
        return None
    if idx > len(my_list):
        return None
    for list in range(len(my_list)):
        if list == idx:
            return my_list[list]
