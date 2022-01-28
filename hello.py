#!/usr/bin/env python3

import os
import json

# print out all env variables as plain text
# print('Content-Type: text/plain') #let the browser know to expect plain text
# print()
# print(os.environ)

# print out env variables as json
#print('Content-Type: application/json') #let the browser know to expect json
#print()
#print(json.dumps(dict(os.environ), indent=2)) # indent=2 for nice formatting

#print query parameter data in html
# print('Content-Type: text/html') #let the browser know to expect html
# print()
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

#print user's browser in html
print('Content-Type: text/html') #let the browser know to expect html
print()
print(f"<p>HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")