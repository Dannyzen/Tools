#simple random email generator using my sailthru address (danny rosen 4/10/2012)
#usage: dummy.py -n # - outputs to a fakes.txt file.
#twitter: @dannyzen
import argparse
parser = argparse.ArgumentParser(description='Docs docs docs these are my docs')
parser.add_argument('-n','--n_variable', type=int, help='Number of fake emails to create', required=True)
args = vars(parser.parse_args())

f = open('fakes.txt','w')
template = 'danny+test%03d@sailthru.com\n'
x = args['n_variable']
f.writelines(template % (x+1) for x in range(x))
