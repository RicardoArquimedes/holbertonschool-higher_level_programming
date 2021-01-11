#!/usr/bin/python3
"""sends a request to the URL and displays the body of
the response"""
import sys
import urllib.request


if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            url = response.read()
            print(url.decode('utf-8'))

    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
