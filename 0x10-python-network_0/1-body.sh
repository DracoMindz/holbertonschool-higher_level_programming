#!/bin/bash
# takes a URL, sends a GET request, displays body of response

if [ $'(curl -L -s -X HEAD  -w "%{http_code}""$1")' == '200' ]
then
    curl -Ls "$1"
fi