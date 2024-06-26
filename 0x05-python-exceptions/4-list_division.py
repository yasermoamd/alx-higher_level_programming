#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ function that divides el by el of lists"""
    results = []
    for i in range(0, list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            results.append(res)
    return (results)
