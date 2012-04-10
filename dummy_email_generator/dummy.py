#simple random email generator using my sailthru address (danny rosen 4/10/2012)
import argparse
parser = argparse.ArgumentParser(description='Docs docs docs these are my docs')
parser.add_argument('-n','--n_variable', type=int, help='Number of fake emails to create', required=True)
args = vars(parser.parse_args())

f = open('foo.txt','w')

x = args['n_variable']
print x
while x != 0:
    x = x - 1
    f.write ("danny+test" + str(x) + "@sailthru.com\n")

