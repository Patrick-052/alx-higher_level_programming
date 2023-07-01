#!/usr/bin/python3
"""Sending a POST request containing an email in the url"""
import urllib.request as ur
import urllib.parse as up
from sys import argv


if __name__ == "__main__":
    email = argv[2]
    value = {'email': email}
    data = up.urlencode(value).encode('utf-8')
    req = ur.Request(argv[1], data)
    with ur.urlopen(req) as res:
        ret = res.read().decode('utf-8')
        print(f"Your email is: {email}")
