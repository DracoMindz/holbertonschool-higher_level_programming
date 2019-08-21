#!/bin/bash
#Script sends a request to URL, as argument, displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
