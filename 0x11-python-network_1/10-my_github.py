#!/usr/bin/python3
"""
Module Name: 10-my_github.py
Description: Takes GitHub username and password and uses the GitHub API
             to display my id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username, passwd = sys.argv[1:]
    auth = HTTPBasicAuth(username, passwd)
    res = requests.get(f'https://api.github.com/users/{username}', auth=auth)

    print(res.json().get('id'))
