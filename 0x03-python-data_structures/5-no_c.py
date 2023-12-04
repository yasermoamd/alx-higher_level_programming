#!/usr/bin/python3
def no_c(my_string):
    new_list = ''
    for i in my_string:
        new_list += "" if i == 'c' or i == 'C' else i
    return new_list
