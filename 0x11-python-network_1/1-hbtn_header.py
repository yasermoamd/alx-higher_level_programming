#!/usr/bin/python3
""" script take url and display the value of x-request-id """
import urllib.request
import sys


if __name__ == "__main__":
    """ script take url and display the value of x-request-id """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
