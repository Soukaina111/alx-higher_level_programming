#!/usr/bin/python3
""" script that takes in a URL, sends a request to
    the URL and displays the body
    of the response (decoded in utf-8)."""

from urllib.request import Request, urlopen
from sys import argv
from urllib.error import HTTPError

if __name__ == "__main__":
    Link = argv[1]
    req = Request(Link)
    try:
        with urlopen(req) as response:
            html = response.read()
            resp_body = html.decode("ascii")
            print(resp_body)
    except HTTPError as er:
        print("Error code:", er.code)
