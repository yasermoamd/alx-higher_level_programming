#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    """fetches https://intranet.hbtn.io/status"""
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        body_str = body.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body_str))
