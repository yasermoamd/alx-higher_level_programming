#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set()
    
    for num in my_list:
        new_set.add(num)
    res = sum(new_set)
    return res
