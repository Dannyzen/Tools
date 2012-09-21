#Usage: python milestone_manager.py -p <Project> -m <Milestone Name> (optional: rm True | False (default is false))
#todo: handling of adding milestones that have been deleted.
import fbSettings
from fogbugz import FogBugz
import argparse

fogbugz = FogBugz(fbSettings.URL)
fogbugz.logon(fbSettings.Login, fbSettings.pw)

parser = argparse.ArgumentParser(description='Usage: python milestone_maker -p <Project> -m <Milestone Name> -rm True|False (Default is false)')
parser.add_argument('-p','--project', type=str, help='Project Name', required=True)
parser.add_argument('-m','--milestone', type=str, help='New Milestone name', required=True)
parser.add_argument('-rm','--delete',type=bool, help='Delete the milestone', default=False,required=False)
args = parser.parse_args()

project_map = {}
projects = fogbugz.listProjects()
for item in projects.findAll('project'):
	 proj_number =  item.ixproject.string.encode('UTF-8') 
	 proj_name = item.sproject.string.encode('UTF-8')
	 project_map.update({proj_name:proj_number})

milestone_map = {}
milestones = fogbugz.listFixFors()
for item in milestones.findAll('fixfor'):
	 milestone_number =  item.ixfixfor.string.encode('UTF-8') 
	 milestone_name = item.sfixfor.string.encode('UTF-8')
	 milestone_map.update({milestone_name:milestone_number})
try:
	 project_id = project_map[args.project]
except KeyError:
	 raise KeyError("Unknown Project Name. Project name must be case sensitive. ")

if args.delete == True :
	 try:
		  milestone_id = milestone_map[args.milestone]
	 except KeyError:
		  raise KeyError("Milestone doesn't exist")
	 milestone = fogbugz.editFixFor(ixfixfor=milestone_id,sfixfor=args.milestone,fAssignable=0)
else:
	 milestone = fogbugz.newFixFor(ixproject=project_id,sfixfor=args.milestone,fAssignable=1)

if milestone.finactive.string == "false":
	 print "Milestone created"
	 
if milestone.finactive.string == "true":
	 print "Milestone deleted"


