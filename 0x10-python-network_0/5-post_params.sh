#!/bin/bash
#Script send a POST request passed to URL; variables: email, subject
curl -X POST -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD""$1"
