#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    """fetches https://intranet.hbtn.io/status"""
    req_status = Request("https://intranet.hbtn.io/status")
    with urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
