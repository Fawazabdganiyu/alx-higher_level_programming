#!/usr/bin/python3
"""
Module Name: 6-post_email.py
Description: Sends a POST request to a given URL with email parameter and
             displays the body of the response (decoded in utf-8)
"""
import sys
import requests

if __name__ == '__main__':
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
