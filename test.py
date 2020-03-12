#!/usr/bin/env python3 

import argparse 
from pprint import *
import sys
import requests 
import json

# parser = argparse.ArgumentParser(description='Json parser')
# parser.add_argument('string',metavar="<provide url here>", help= "Argv1 = provide url to parse")
# args = parser.parse_args()

baseurl = "https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json"

def parser(url):
	req = requests.get(url)
	op = json.loads(req.content)
	return op

output = parser(baseurl)

print ("#####################Task1 Output#########################\n")
pprint (output)

print ("#####################Task2 Output#########################\n")
# print type(output)
for element in output:
	if element["id"] == 107:
		pprint (element)
#### Task 2 can be also achievable by below ###################
# pprint (output[6])


