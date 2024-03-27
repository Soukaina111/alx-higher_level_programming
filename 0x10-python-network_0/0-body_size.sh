#!/bin/bash
# This script resent the  request to the same URlthat it come from
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
