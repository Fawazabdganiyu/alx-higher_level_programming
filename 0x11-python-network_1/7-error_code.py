#!/usr/bin/python3
"""
Module Name: 3-error_code.py
Description: Sends a request to a URL and displays the body of the response
             decoded in `utf-8`
"""
import sys
import requests

if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)
