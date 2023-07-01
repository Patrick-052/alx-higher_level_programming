#!/usr/bin/python3
"""Sending a POST request containing an email in the url"""
import urllib.request as ur
import urllib.parse as up
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}
    data = up.urlencode(value).encode('ascii')
    with ur.urlopen(argv[1], data) as res:
        ret = res.read().decode('utf-8')
        print(ret)
