"""
Random Assignment

When you have cases that are handled by multiple individuals on a team,
it can be difficult to distribute the tasks evenly to each member without
cherry picking or having someone manage the queue.

This script helps by taking cases assigned to an "Up For Grabs" user and
re-assigning them randomly to the members of the team, based on a specified
weight.

How to use this script:
1. Set up a Virtual User called "Up For Grabs" within FogBugz.
2. Make the "Up For Grabs" user the primary contact for the support area
   you are using.
3. Change the settings below to correspond to your installation.
4. Run this script using:
   > python randomAssignment.py
   
See https://developers.fogbugz.com/default.asp?W194 for more
information on using the FogBugz XML API with Python.
"""

IX_PERSON_UP_FOR_GRABS = 53 # the ixPerson value of the Up For Grabs user
#IX_AREA_SUPPORT        = 36 # the ixArea value of the cases in your support queue
REPS = { 25 : ['Danny Test',1],     # a list of team members, using this format:
     52 : ['Eric Test', 1]}       # { ixPerson : [name, weight]...

import re
from fogbugz import FogBugz
import fbSettings
import random 
from random import choice

#log onto FogBugz 
print fbSettings.Login, fbSettings.pw
fogbugz = FogBugz(fbSettings.URL)
fogbugz.logon(fbSettings.Login, fbSettings.pw)


#lottery is an array to help with randomness
lottery = []
#this will fill the lottery array with the ixPerson values in REPS,
#one for each "weight" value above

testers = []

for rep in REPS:
  #lottery.extend([rep] * REPS[rep][1])
  testers.append(rep)

print testers

#shuffle the list
random.shuffle(lottery)

searchString = 'assignedto: "=%s"' % (IX_PERSON_UP_FOR_GRABS)
#setfilter = fogbugz.setCurrentFilter(sFilter=130)
respUpForGrabs = fogbugz.search(q=searchString,cols='ixBug,ixPersonOpenedBy')





for case in respUpForGrabs.cases.childGenerator():
	print case 
	exit()
	if case['ixpersonopenedby'] in testers:
		target_rep = case['ixpersonopenedby']
		#print target_rep, "goes to", case['ixpersonopenedby']
	else:
			target_rep = choice(testers)
			#print target_rep, "goes to", case['ixpersonopenedby']
	fogbugz.assign(ixBug=case.ixbug.string,ixPersonAssignedTo=target_rep)
    
	#if the person who last edited the case assigned it to the Up For Grabs user,
    #we want to keep iterating through the lottery until we get a different user.

#while target_rep == case.ixPersonOpenedBy: 
#        target_rep = lottery[i % len(lottery)]
#        i += 1

