#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
"""

import requests
from sys import argv

if __name__ == "__main__":
    Link = argv[1]
    req = requests.get(Link)
    head = req.headers
    print(head.get("X-Request-Id"))
