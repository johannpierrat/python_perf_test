import timeit

code1 ='''
tab = [None] * 100
for i in xrange(len(tab)):
    tab[i] = 1
'''

code2 ='''
tab = []
for i in xrange(100):
    tab.append(1)
'''

print "1D Array"
time1 = timeit.Timer(code1).timeit()
time2 = timeit.Timer(code2).timeit()

print "Array initialize %fs" % time1
print "Array append %fs" % time2

print "2D Array"
code1 = '''
tab = [[None] * 10] * 10
for i in xrange(len(tab)):
    for j in xrange(len(tab[i])):
        tab[i][j] = 1
'''

code2 = '''
tab = [[]] * 10
for i in xrange(len(tab)):
    tab[i] = [None] * 10
    for j in xrange(len(tab[i])):
        tab[i][j] = 1
'''

time1 = timeit.Timer(code1).timeit()
time2 = timeit.Timer(code2).timeit()

print "Array initialized 2d Once %fs" % time1
print "Array initialized 1d      %fs" % time2
