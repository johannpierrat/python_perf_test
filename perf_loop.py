#!/usr/bin/python2.7

import timeit

code1='''
i = 0
while i < len(a):
    a[i] = 1
    i = i + 1
'''

code2='''
i = 0
while 1:
    try:
        a[i] = 1
        i = i + 1
    except IndexError:
        break;
'''


print("test if")
time1 = timeit.Timer(code1, setup='a = [10]*100').timeit()
print ("Test try")
time2 = timeit.Timer(code2, setup='a = [10]*100').timeit()

print("with if  %fs" % time1)
print("with try %fs" % time2)
