#!/usr/bin/python3
""" function that prints the first x
    elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    count_length = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            count_length += 1
        except (ValueError, TypeError):
            continue
    print()
    return (count_length)
