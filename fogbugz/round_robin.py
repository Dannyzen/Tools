#!/usr/bin/python2.7

import fbSettings
from fogbugz import FogBugz
from random import choice
from random import shuffle
from time import sleep
from time import strftime

IX_PERSON_UP_FOR_GRABS = 53 # the ixPerson value of the Up For Grabs user
IX_AREA_SUPPORT        = 36 # the ixArea value of the cases in your support queue
REPS = { 25 : ['Danny Test',1],     # a list of team members, using this format:
     52 : ['Eric Test', 1]}       # { ixPerson : [name, weight]...

#Log onto FogBugz 
print "Logging in..."
fogbugz = FogBugz(fbSettings.URL)
fogbugz.logon(fbSettings.Login, fbSettings.pw)
assignment = {}
#Add users and current assignment count to dictionary.
for rep in REPS:
  searchString = 'assignedto: "=%s" status:"Reviewed"' % (rep)
  num = str(fogbugz.search(q=searchString)).split('"')
  assignment[rep] = num[1]
for user in assignment:
  print user, "has", assignment[user], "assignment(s)!"
#Code for assignment is only scaleable up to this point. Per convo w/ Danny, we will review this and make necessary edits once we hire more automation engineers.
sum = int(assignment.values()[0])-int(assignment.values()[1])
#Obtain all tickets assigned to our main QA user.
searchString = 'assignedto: "=%s"' % (IX_PERSON_UP_FOR_GRABS)
grabs = fogbugz.search(q=searchString)
tickets = []
for case in grabs.cases.childGenerator():
  tickets.append(case['ixbug'])
#Assign as necessary
print len(tickets), "total tickets..."
c = 0
try:
  if sum < 0:
    print assignment.keys()[0], "needs", str(sum).strip('-'), "more!"
    searchString = 'assignedto: "=%s"' % (assignment.keys()[0])
    sum = str(sum).strip('-')
    while c < int(sum):
      fogbugz.assign(ixBug=tickets[c],ixPersonAssignedTo=assignment.keys()[0])
      data = tickets[c]
      tickets.remove(data)
      c=c+1
      print "Initial Assignment:", tickets[c], "to", assignment.keys()[0]
  elif int(sum) > 0:
    print assignment.keys()[1], "needs", str(sum).strip('-'), "more!"
    searchString = 'assignedto: "=%s"' % (assignment.keys()[1])
    sum = str(sum).strip('-')
    while c < int(sum):
      fogbugz.assign(ixBug=tickets[c],ixPersonAssignedTo=assignment.keys()[1])
      data = tickets[c]
      tickets.remove(data)
      c=c+1
      print "Initial Assignment:", tickets[c], "to", assignment.keys()[1]
  elif sum == 0:
    print "Assignment counts are equal. Continuing..."
  else:
    print "There was a problem calculating current assignments..."
    exit()
except IndexError:
  print len(tickets), "tickets available... Please assign some..."
#Reset count and assign tickets evenly.
c = 0
shuffle(tickets)
total = len(tickets)
print total, "tickets left..."
users = [assignment.keys()[0],assignment.keys()[1]]
while c < total:
  try:
    for user in users:
      fogbugz.assign(ixBug=tickets[c],ixPersonAssignedTo=user)
      data = tickets[c]
      print "Assigned", data, "to", user
      c=c+1
  except IndexError:
    print "."
    break
print "Round Robin completed -", strftime("%m/%d/%Y %H:%M:%S")