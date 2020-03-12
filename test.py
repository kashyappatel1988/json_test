#!/usr/bin/env python3 

import argparse 
from pprint import *
import sys
import requests 

parser = argparse.ArgumentParser(description='Json parser')
parser.add_argument('string',metavar="<provide url here>", help= "Argv1 = provide url to parse")
args = parser.parse_args()

baseurl = str(sys.argv[1])
# baseurl = "https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json"
def parser(url):
	req = requests.get(url)
	return req.content


pprint (parser(baseurl))