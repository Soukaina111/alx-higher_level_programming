#!/usr/bin/python3
"""
    This script  takes in a URL and an email address, sends a POST
    request to the passed URL with the email as a
    parameter, and finally displays the body of the response.
"""
import requests
from sys import argv

if __name__ == "__main__":
    Link, email = argv[1], argv[2]
    resp = requests.post(Link, data={"email": email})
    outcome = resp.text
    print(outcome)
