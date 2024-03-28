#!/usr/bin/python3
"""
 This script your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""

import requests
import requests.auth
from sys import argv


if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
    link = "https://api.github.com/user"
    req = requests.get(link, auth=auth)
    dat = req.json()
    print(dat.get("id"))
