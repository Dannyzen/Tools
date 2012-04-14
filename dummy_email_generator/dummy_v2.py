#simple random email generator using my sailthru address (danny rosen 4/10/2012)
#usage: dummy.py -n # -e (prod,qa,dev) outputs to a fakes.txt file.
#twitter: @dannyzen
from sailthru import sailthru_client as sc
import argparse
import json
  
template = 'danny+test%03d@sailthru.com'

env_urls = {
    "qa": "http://api.sailthru-qa.com",
    "prod": "http://api.sailthru.com",
    "dev": "http://api.sailthru-dev.com",
}

parser = argparse.ArgumentParser(description='Docs docs docs these are my docs')
parser.add_argument('-n','--n_variable', type=int, help='Number of fake emails to create', required=True)
parser.add_argument('-e','--e_variable', type=str, help='Environment', required=True)
args = vars(parser.parse_args())
num = args['n_variable']
env = args['e_variable']

json_data=open('/Users/robertrosen/d.txt')
data = json.load(json_data)
api_key=(data["api_key"])
api_secret=(data["api_secret"])
json_data.close()

# a list of e-mails
emails = [template % (num+1) for num in range(num)]

# the name of the list, used as filename also
fname = ("%d_person_list" % num)

# A comma-separated list of emails as a string, See
# http://docs.sailthru.com/api/job#import
file_content = ','.join(emails)

f = open(fname,'w+')
f.writelines("emails\n")
f.writelines('%s\n' for x in emails)

try:
    env_url = env_urls[env]
except KeyError:
    raise KeyError("Unknown or unspecified environment %r" % env)

sailthru_client = sc.SailthruClient(api_key, api_secret, env_url)
data={"job": "import","list":fname,"emails":file_content}
response = sailthru_client.api_post('job',data)
print response
print fname
