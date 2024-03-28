#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    and displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    Link = argv[1]
    req = requests.get(Link)
    req_status = req.status_code

    if req_status < 400:
        print(req.text)
    else:
        print("Error code:", req.status)
