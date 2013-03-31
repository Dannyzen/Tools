from sailthru import sailthru_client as sc
import json as json
import argparse
from pprint import pprint

env_urls = {
    "qa2": "http://api.qa2.sailthru-qa.com",
    "prod": "http://api.sailthru.com",
    "dev": "http://api.sailthru-dev.com",
}

parser = argparse.ArgumentParser(description='Docs docs docs these are my docs')
parser.add_argument('-e','--e_variable', type=str, help='Environment', required=True)
args = parser.parse_args()
env = args.e_variable

#open the data file with the api info
with open('../../d.txt') as json_data:
    data = json.load(json_data)
    api_key = data["api_key"]
    api_secret = data["api_secret"]
#assure the args are valid, and if they are assign the env url accordingly
try:
    env_url = env_urls[env]
except KeyError:
    raise KeyError("Unknown or unspecified environment %r" % env)
sailthru_client = sc.SailthruClient(api_key, api_secret, env_url)
response = sailthru_client.api_get('list', data)

#[ (the thing I want) for (variable to iterate) in (some other list)]
rmlist=([l['name'] for l in body['lists']]) 
for list_name in rmlist:
	todelete={"list":list_name}
	response = sailthru_client.api_delete('list', todelete)
	print response.get_body()
