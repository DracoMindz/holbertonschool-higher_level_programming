#!/bin/bash
# Takes in URL displays HTTP methods URL server will accept
curl -sI "$1" | sed -n 's/Allow: //p'