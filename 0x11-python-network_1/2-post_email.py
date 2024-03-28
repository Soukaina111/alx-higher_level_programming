#!/usr/bin/python3
""" This script  takes in a URL and an email,
    sends a POST request to the passed
    URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)"""

from urllib.request import Request, urlopen
from sys import argv
from urllib.parse import urlencode

if __name__ == "__main__":
    Link = argv[1]
    val = {"email": argv[2]}
    info = urlencode(val).encode("ascii")
    req = Request(Link, info)
    with urlopen(req) as response:
        html = response.read()
        resp_body = html.decode("utf-8")
        print(resp_body)
