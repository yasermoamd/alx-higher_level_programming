#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is not None:
        revered_list = my_list[:]
        if idx < 0 or idx >= len(my_list):
            return revered_list
        revered_list[idx] = element
        return revered_list
