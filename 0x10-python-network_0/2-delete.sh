#!/bin/bash
# Send delete request as first argument display body response
curl -sI "$1"| sed -n 's/Allow: //p'
