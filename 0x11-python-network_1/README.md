# 0x11. Python - Network #1

## Learning Objectives
At the end of this project , you are expected to be able to explain to anyone, without the help of Google: 

### General
How to fetch internet resources with the Python package urllib
How to decode urllib body response
How to use the Python package requests #requestsiswaysimplerthanurllib
How to make HTTP GET request
How to make HTTP POST/PUT/etc. request
How to fetch JSON resources
How to manipulate data from an external service

## Requirements

### General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
Your code should not be executed when imported (by using if __name__ == "__main__":)

## Tasks
**0. What's my status? #0 mandatory**
Write a Python script that fetches https://<website>.io/status

**1. Response header value #0 mandatory**
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

**2. POST an email #0 mandatory**
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response 

**3. Error code #0 mandatory**
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response 

**4. What's my status? #0 mandatory**
Write a Python script that fetches https://<website>.io/status using the requests package.

**5. Response header value #1 mandatory**
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.
(request package)

**6. POST an email #1 mandatory**
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
(request package)

**7. Error code #1 mandatory**
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
(request package)

**8. Search API mandatory**
Write a Python script that takes in a letter and sends a POST request to http://<IP:Host>/search_user with the letter as a parameter.

**9. Star Wars API #0 mandatory**
Write a Python script that takes in a string and sends a search request to the Star Wars API

**10. My Github! mandatory**
Write a Python script that takes your Github credentials (username and password) and uses the Github API to display your id

