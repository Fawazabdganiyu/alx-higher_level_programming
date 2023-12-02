#!/usr/bin/python3
"""
Module Name: 10-my_github.py
Description: Takes GitHub username and password and uses the GitHub API
             to display my id
"""
import sys
import requests

if __name__ == '__main__':
    username, passwd = sys.argv[1:]
    headers = {}
    headers['Accept'] = "application/vnd.github+json"
    headers['Authorization'] = f"Bearer {passwd}"
    headers['X-GitHub-Api-Version'] = "2022-11-28"
    res = requests.get(f'https://api.github.com/users/{username}',
                       headers=headers)

    print(res.json().get('id'))
