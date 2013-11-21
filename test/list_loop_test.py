#!/usr/bin/python2.7

import timeit

setup='''
import random

a = random.sample(xrange(1000), 100)
'''

code1='''
b = []
for i in a:
    b.append(i)
'''

code3='''
b = []
map(b.append, a)
'''

print("test 1: simple")
time1 = timeit.Timer(code1, setup=setup).timeit()
print("test 2: array")
time2 = timeit.Timer('b = [i for i in a]', setup=setup).timeit()
print("test 3: map")
time3 = timeit.Timer(code3, setup=setup).timeit()
print("simple loop: %fs" % time1)
print("array loop: %fs" % time2)
print("map loop: %fs" % time3)
