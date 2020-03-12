#!/usr/bin/env python3 

import argparse 
from pprint import *
import sys
import requests 
import json
l = []
parser = argparse.ArgumentParser(description='Json parser')
parser.add_argument('-s',action="store",dest="session_id",default=107,metavar="<session id>", type = int,
	help= "Provide an integer to get status by session id")
parser.add_argument('-d',action="store",dest="device_id",default="3",metavar="<device id>", type = int,
	help= "Provide an integer to get status by device id")

args = parser.parse_args()
# print (args.device_id)
# print (args.session_id)
baseurl = "https://transit-sessions.s3-us-west-2.amazonaws.com/sessions.json"

### function to do an API call to the give url 

def parser(url):
	req = requests.get(url)
	op = json.loads(req.content)
	return op

output = parser(baseurl)

print ("\n#####################Task1 Output#########################\n")

pprint (output) 

print ("\n#####################Task2 Output#########################\n")
# # print type(output)
# for element in output:
# 	if element["id"] == 107:
# 		pprint (element)
def session_id(id_number):
	for element in output:
		if element["id"] == int(id_number):
			return element
pprint (session_id(107))
#### Task 2 can be also achievable by below ###################
# pprint (output[6])
print ("\n#####################Task3 Output session id =107###################################\n")
def getstatus(dict):
	if int(dict['status']) == 0:
		print ("OK")
	else:
		print ("CRITICAL")

getstatus(session_id(107))	
# if session_id(107)['status'] == 0:
# 	print "OK"
# else:
# 	print "CRITICAL"

print ("\n#####################Task4 Output device id = 3######################################\n")

def getstatusbydeviceid(deviceid):
	l=[]
	for element in output:
		if element["device_id"] == str(deviceid):
			getstatus(element)			

getstatusbydeviceid(3)

print ("\n#####################Task5 Output by session id = %s#########################\n"%(args.session_id))

getstatus(session_id(args.session_id))

print ("\n#####################Task5 Output by device id = %s #########################\n"%(args.device_id))
getstatusbydeviceid(args.device_id)
