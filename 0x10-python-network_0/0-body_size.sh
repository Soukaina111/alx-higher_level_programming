#!/bin/bash
# This script resent the  request to the same URlthat it come from
# While displaying the size of the response's body
 

curl -sI $1 | grep "Content-Length" | cut -d " " -f2
