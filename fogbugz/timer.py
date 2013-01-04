from fogbugz import FogBugz
from fogbugz import FogBugzAPIError
import fbSettings
import argparse
import pprint
from BeautifulSoup import BeautifulSoup

if hasattr(fbSettings,'TOKEN'):
	fogbugz = FogBugz(fbSettings.URL, fbSettings.TOKEN)
else:
    fogbugz = FogBugz(fbSettings.URL)
    fogbugz.logon(fbSettings.LOGIN, fbSettings.PW)

parser = argparse.ArgumentParser(description='I fix this later')
parser.add_argument('-t','--ticket', required=True, help='Ticket Number')
parser.add_argument('-e','--end', action='store_true', default=False, help='End')

args = parser.parse_args()

def stopWork(ticket):
    response = fogbugz.stopWork(ixBug=ticket)
    print "Stopped working on ticket " + ticket

def setEst(ticket,estimate):
    query=(str(ticket))
    response = fogbugz.edit(ixBug=ticket,hrsCurrEst=estimate)
    return estimate

def startWork(ticket):
    try:
        if getTime(ticket) != 0:
            response = fogbugz.startWork(ixBug=ticket)
            print "Started working on ticket " + ticket
    except FogBugzAPIError:
        #In the case an estimate isn't set, get it from the user
        est = setEst(ticket,input("How long is this going to take you (in hours)? :"))
        #And then start work
        response = fogbugz.startWork(ixBug=ticket)
        print "Started working on " + args.ticket

def getTime(ticket):
    query = (str(ticket))
    response = fogbugz.search(q=query,cols="hrsCurrEst")
    return response.hrscurrest.string.encode('UTF-8')

#If you want to end the time, go ahead. Otherwise you're starting.
if args.end:
    stopWork(args.ticket)
else:
    startWork(args.ticket)
