#!/bin/bash
# This script  takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
header="X-School-User-Id: 98"
curl -sH "$header" $1
