#!/usr/bin/python3
""" Write a Python script that takes in a URL and an email
sends a POST request to the passed URL"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":

    body = urllib.parse.urlencode({'email': sys.argv[2]})
    body = body.encode('ascii')

    with urllib.request.urlopen(sys.argv[1], body) as response:
        header = response.read()
        print(header.decode('utf-8'))
