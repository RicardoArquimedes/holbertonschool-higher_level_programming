#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user"""
import sys
import requests as rq


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    r = rq.post(url, data={'q': q})
    try:
        data = r.json()
        if data:
            print('[{}] {}'.format(data['id'], data['name']))

        else:
            print('No result')
    except:
        print('Not a valid JSON')
