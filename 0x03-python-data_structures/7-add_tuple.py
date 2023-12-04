#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    if (len(tuple_a) < 2):
        if len(tuple_a) == 0:
            n1 = 0
            n2 = 0
        else:
            n1 = tuple_a[0]
            n2 = 0
    else:
        n1 = tuple_a[0]
        n2 = tuple_a[1]

    if (len(tuple_b) < 2):
        if len(tuple_b) == 0:
            m1 = 0
            m2 = 0
        else:
            m1 = tuple_a[0]
            m2 = 0
    else:
        m1 = tuple_b[0]
        m2 = tuple_b[1]
    return (n1 + m1, n2 + m2)
