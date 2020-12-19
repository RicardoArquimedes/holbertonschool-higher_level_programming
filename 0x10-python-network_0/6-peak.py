#!/usr/bin/python3
""" find a peak funct"""

def find_peak(integer_list):
    """ sorted peak"""
    if len(integer_list) == 0:
        return None
    integer_list.sort()
    return integer_list[-1]
