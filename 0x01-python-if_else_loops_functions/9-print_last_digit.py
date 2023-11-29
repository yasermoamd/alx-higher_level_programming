#!/usr/bin/python3
def print_last_digit(number):
    number = number if number > 0 else -1 * number
    last = number % 10
    print("{}".format(last), end='')
    return (last)
