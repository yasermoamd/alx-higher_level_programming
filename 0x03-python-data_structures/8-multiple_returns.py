#!/usr/bin/python3

def multiple_returns(sentence):
    c = ()
    if len(sentence) == 0:
        x = 0, "None"
    else:
        x = len(sentence), sentence[0]
    return (x)
