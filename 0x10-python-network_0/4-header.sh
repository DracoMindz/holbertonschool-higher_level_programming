#!/bin/bash
#takes URL as argument, sends GET request, display body response
curl -sL -H "X-HolbertonSchool-User-Id: 98" "$1"
