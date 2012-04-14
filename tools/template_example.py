def visits(name, n):
    """ adds an s to 'time' if n > 1 """
    return "%s visited you %d time%s" % (name, n, ['','s'][n>1])

print( visits("Harry", 1))
print( visits("Lorie", 3))
