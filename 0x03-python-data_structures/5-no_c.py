#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for c in my_string.lower():
        if c == 'c':
            c = ''
        result += c
    return result
