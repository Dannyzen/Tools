#simple random email generator using my sailthru address (danny rosen 4/10/2012)
#usage: dummy.py -n # -e (prod,qa,dev) outputs to a fakes.txt file.
#twitter: @dannyzen
from sailthru import sailthru_client as sc
import random
import string
from time import time
from datetime import datetime
import argparse
import json
import os.path

json_data=open('/Users/robertrosen/d.txt')
data = json.load(json_data)
api_key=(data["api_key"])
api_secret=(data["api_secret"])
json_data.close()

parser = argparse.ArgumentParser(description='Docs docs docs these are my docs')
parser.add_argument('-n','--n_variable', type=int, help='Number of fake emails to create', required=True)
parser.add_argument('-e','--e_variable', type=str, help='Environment', required=True)
args = vars(parser.parse_args())
num = args['n_variable']
env = args['e_variable']

fname= (str(num) + "_person_list")
	
f = open(fname,'w+')
file_content = (f.readlines())


template = 'danny+test%03d@sailthru.com\n'
f.writelines("emails\n")
f.writelines(template % (num+1) for num in range(num))

if env == "qa":
	env_url = "http://api.sailthru-qa.com"
elif env =="prod":
	env_url = "http://api.sailthru.com"
elif env =="dev":
	env_url = "http://api.sailthru-dev.com"
else:
	print "i need an environment"

sailthru_client = sc.SailthruClient(api_key, api_secret,env_url)
data={"job": "import","list":fname,"emails":file_content}
response = sailthru_client.api_post('job',data)
print response
print fname
