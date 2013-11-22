#!/usr/bin/python2.7

import timeit

code1='''
for i in xrange(len(a)):
    for j in xrange(len(a[i])):
        a[i][j] = a[i][j] + 1
'''

setup='''
import random

a = [[0]] * 100
for i in xrange(len(a)):
    a[i] = [0] * 10

def test1(tab):
    for j in xrange(len(tab)):
        tab[j] = tab[j] + 1
'''

print("Test native")
time1 = timeit.Timer(code1, setup=setup).timeit()
print("Test map")
time2 = timeit.Timer('map(test1, a)', setup=setup).timeit()

print("Native:     %fs" % time1)
print("Map:        %fs" % time2)
print("Diffenrece: %fs" % abs(time2 - time1))
