#!/usr/bin/python3
"""sending a request to the URL and displaying the
   body of the response and handling HTTPError"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    scd = res.status_code
    if scd >= 400:
        print(f"Error code: {scd}")
    else:
        print("res.text")
