#!/usr/bin/python3
"""
     This script takes in a letter and sends a POST request to
     http://0.0.0.0:5000/search_user
     with the letter as a parameter
"""
from sys import argv
import requests


def send_post_request(Link, charge):
    resp = requests.post(Link, data=charge)
    return resp


def process_response(response):
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get("id"), data.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("Error code:", response.status_code)


if __name__ == "__main__":
    Lin = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        word = ""
    else:
        word = argv[1]
    char = {"q": word}
    respo = send_post_request(Lin, char)
    process_response(respo)
