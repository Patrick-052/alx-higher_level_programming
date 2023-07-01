#!/usr/bin/python3
"""Sending an email to a url
   and printing the response's body"""
import requests
from sys import argv


if __name__ == "__main__":
    params = {'email': argv[2]}
    res = requests.post(argv[1], data=params)
    print(res.text)
