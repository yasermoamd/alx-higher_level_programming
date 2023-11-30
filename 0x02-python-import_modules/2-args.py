#!/usr/bin/python3 
"""Print the number of and list of arguments."""
import sys

word = len(sys.argv) - 1
if word == 0:
    print("0 arguments.")
elif word == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(word))
for i in range(word):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
