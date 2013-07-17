# usage: genDynamicEmails.py <#ofemails> 
# (ie: python genDanymicEmails.py 4)

import sys
from faker import Faker

fake = Faker()

num = int (sys.argv[1])
def genMails(num):
    x = 0
    while x < num: 
            print (fake.firstName() + "@" + str(x) + fake.domainName())
            x = x + 1
genMails(num)
