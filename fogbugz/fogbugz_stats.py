from fogbugz import FogBugz
import fbSettings
import argparse, sys
import pprint

fogbugz = FogBugz(fbSettings.URL)
fogbugz.logon(fbSettings.LOGIN, fbSettings.PW)
parser = argparse.ArgumentParser(description='I fix this later')
parser.add_argument('-m','--milestone', metavar='A list of Milestones by name, seperated by space(ie: ui release/9.0 link-php release/9.0)',
                    nargs ='+',
                    help='Milestone Names', required=False)
parser.add_argument('-l','--list',action='store_true', default=False,
                    help='List the available milestones')

args = parser.parse_args()
pp = pprint.PrettyPrinter(indent=4)

milestone_map = {}
milestones = fogbugz.listFixFors()
for item in milestones.findAll('fixfor'):
     number =  item.ixfixfor.string.encode('UTF-8')
     name = item.sfixfor.string.encode('UTF-8')
     milestone_map.update({name:number})

if args.list:
    pp.pprint(milestone_map)

ms = "test1"
tickets_per_milestone = {}
#print args.milestone
if args.milestone:
    for milestone_name in args.milestone:
        try:
            current_milestone = milestone_map[milestone_name]
            query = ('milestone:' + current_milestone)
            response = (fogbugz.search(q=query))
            ticket_quantity = response.cases['count']
            tickets_per_milestone.update({current_milestone:ticket_quantity})
        except KeyError:
            raise KeyError("I donno this milestone")
if len(tickets_per_milestone.keys())>0:
    pp.pprint(tickets_per_milestone)
