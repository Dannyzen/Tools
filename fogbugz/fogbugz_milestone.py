#Usage: python fogbugz_milestone.py --o old milestone -n new milestone
from fogbugz import FogBugz
import datetime
import re
import argparse
import json


parser = argparse.ArgumentParser(description='Docs docs docs these are my docs')
parser.add_argument('-o','--o_variable', type=str, help='Old Milestone name', required=True)
parser.add_argument('-n','--n_variable', type=str, help='New Milestone name', required=True)
args = parser.parse_args()

fb = FogBugz("https://sailthru.fogbugz.com/") 
with open('../d.txt') as json_data:
	data = json.load(json_data)
	login = data["login"]
	passw = data["pass"]
fb.logon(login,passw)


milestones = fb.listFixFors()

#this is not being used now ... it gets the most current milestone... i could probably trash it..
milestone_dates, sep, tail = milestones.sfixfor.renderContents().partition('T')
miled =  milestones.findAll('dt',limit=2)[1]
work = miled.renderContents().partition('T')
milestone = work[0]
milestone = milestone.replace("-","/")
print milestone 

search = 'milestone'+':'+args.o_variable+' '+'status:open -status:Merged -milestone:Undecided Project:Sailthru'
print search

response = fb.search(q=search)
for case in response.cases.childGenerator():
	print case['ixbug']
#	fb.edit(ixBug=case['ixbug'],sFixFor=args.n_variable)


