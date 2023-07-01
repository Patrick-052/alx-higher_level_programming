#!/usr/bin/python3
"""Print a different request
   id every time a request is made"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    Id = res.headers['X-Request-Id']

    print(Id)
