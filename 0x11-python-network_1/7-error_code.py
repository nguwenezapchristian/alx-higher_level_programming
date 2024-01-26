#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the
URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    try:
        resp = requests.get(sys.argv[1])
        print(resp.text)
    except requests.exception.RequestException as error:
        if error.status >= 400:
            print(f"Error code: {error.status}")
