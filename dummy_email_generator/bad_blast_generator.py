#simple random email generator using my sailthru address (danny rosen 4/10/2012)
#usage: dummy.py -n # -e (prod,qa,dev) outputs to a (num)_person_list.txt file.
#twitter: @dannyzen
from sailthru import sailthru_client as sc
import argparse
import json
  
template = 'sailtest%03d@dannyrosenshardbounce.com'

env_urls = {
    "qa": "http://api.sailthru-qa.com",
    "prod": "http://api.sailthru.com",
    "dev": "http://api.sailthru-dev.com",
}
#go go gadget args
parser = argparse.ArgumentParser(description='Docs docs docs these are my docs')
parser.add_argument('-n','--n_variable', type=int, help='Number of fake emails to create', required=True)
parser.add_argument('-e','--e_variable', type=str, help='Environment', required=True)
args = parser.parse_args()
num = args.n_variable
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

# a list of e-mails
emails = [template % (n+1) for n in range(num)]

# the name of the list, used as filename also. if i dont +1 num it goes foobar, i uh.. dont know why.
fname = ("%d_person_list_bad" % num)

# A comma-separated list of emails as a string, See
# http://docs.sailthru.com/api/job#import
file_content = ','.join(emails)

with open(fname, 'w+') as f:
    f.writelines("emails\n")
    f.writelines(file_content)

sailthru_client = sc.SailthruClient(api_key, api_secret, env_url)
data = {
    "job": "import",
    "list": fname,
    "emails": file_content,
}
response = sailthru_client.api_post('job', data)
print response
