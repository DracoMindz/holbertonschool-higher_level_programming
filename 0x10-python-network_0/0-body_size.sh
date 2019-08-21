#!/bin/bash
#takes a URL, send a request to that URL, display the body of the response
curl -s "$1" | wc -c
