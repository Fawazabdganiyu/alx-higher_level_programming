#!/usr/bin/python3
"""
Module Name: 1-hbtn_header.py
Description: Sends a request to a given URL and displays the value of the
             `X-Request-Id` varibale found in the header of the response
"""
import sys
from urllib.request import Request, urlopen

if __name__ == '__main__':
    req = Request(sys.argv[1])
    with urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
