#!/usr/bin/python3
"""
    pow: function computes a to power of b and return value
    @param: a and b
    return: return value
"""


def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / pow(a, -b)
    elif b % 2 == 0:
        half_pow = pow(a, b // 2)
        return half_pow * half_pow
    else:
        return a * pow(a, b - 1)
