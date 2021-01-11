#!/usr/bin/python3
"""
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
- You are not allow to import other packages than requests and sys
"""
import sys
import requests as rq


if __name__ == "__main__":
    r = rq.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
