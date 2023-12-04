#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for i in range(len(my_list)):
        result.append(True if my_list[i] % 2 == 0 else False)
    return result
