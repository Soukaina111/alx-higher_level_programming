#!/usr/bin/python3
""" This script  sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response."""

from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    Link = argv[1]
    req = Request(Link)
    with urlopen(req) as response:
        html_head = response.headers
        print(dict(html_head).get("X-Request-Id"))
