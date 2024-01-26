#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the
URL and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            page = response.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as status_code:
        print(f"Error code: {status_code}")
