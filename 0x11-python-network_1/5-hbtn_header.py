#!/usr/bin/python3
"""
Module Name: 5-hbtn_header.py
Description: Sends a request to a given URL and displays the value of the
             `X-Request-Id` varibale found in the header of the response
"""
import requests
import sys

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
