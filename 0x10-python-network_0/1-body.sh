#!/bin/bash
# takes a URL, sends a GET request, displays body of response

if [ $'(curl -s -o /dev/null  -w "%{http_code}""$1")' == 200 ]
then
    curl -sL "$1"
fi