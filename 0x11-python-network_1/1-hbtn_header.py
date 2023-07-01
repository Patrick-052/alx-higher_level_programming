#!/usr/bin/python3
"""Displaying a different value of X-Request-Id
   on every call of the request"""
import urllib.request as ur
from sys import argv


if __name__ == "__main__":
    with ur.urlopen(argv[1]) as res:
        Id = res.headers['X-Request-Id']
        print(Id)
