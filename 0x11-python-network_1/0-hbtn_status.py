#!/usr/bin/python3
"""
Module Name: 0-hbtn_status.py
Description: A script that fetches `https://alx-intranet.hbtn.io/status`
"""
from urllib.request import Request, urlopen

if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        res = response.read()
        print("Body response:")
        print(f"    - type: {type(res)}")
        print(f"    - content: {res}")
        content = res.decode('utf-8')
        print(f"    - utf8 content: {content}")
