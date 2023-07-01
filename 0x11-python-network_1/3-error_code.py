#!/usr/bin/python3
"""Sending a request to a specified url and
   displaying the body of the response as well as handling a HTTPError"""
import urllib.request as ur
import urllib.error as uer
from sys import argv


if __name__ == "__main__":
    try:
        with ur.urlopen(argv[1]) as res:
            cont = res.read().decode('utf-8')
            print(cont)
    except uer.HTTPError as e:
        print(f"Error code: {e.code}")
