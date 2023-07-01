#!/usr/bin/python3
"""Displaying the body of a request
   obtained by the requests library"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    cont = res.text

    print("Body response:")
    print(f"\t- type: {type(cont)}")
    print(f"\t- content: {cont}")
