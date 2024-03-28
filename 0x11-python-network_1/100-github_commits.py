#!/usr/bin/python3
"""
 This script answers the "TIME FOR AN INTERVIEW "
 task
"""

import requests
from sys import argv


if __name__ == "__main__":
    repo_name = argv[1]
    repo_owner = argv[2]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    response = requests.get(url)
    commits = response.json()
    for co in commits[:10]:
        sha = co["sha"]
        author_name = co["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
