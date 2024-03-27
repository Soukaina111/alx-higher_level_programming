#!/bin/bash
# This script resent the  request to the same URlthat it come from
# While displaying the size of the response's body

curl -s "$1" -w '%{size_download}\n' -o /dev/null
