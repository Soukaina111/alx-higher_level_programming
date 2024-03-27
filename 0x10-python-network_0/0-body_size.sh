#!/bin/bash
# This script resent the  request to the same URlthat it come from
# While displaying the size of the response's body
 
url1= $1

curl -sI url1 | grep "Content-Length" | cut -d " " -f2
