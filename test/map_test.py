#!/usr/bin/python2.7

import timeit
import sys

def test():
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

    stdout = sys.stdout
    stdout.write("Test native...")
    stdout.flush()
    time1 = timeit.Timer(code1, setup=setup).timeit()
    stdout.write("done!\n")
    stdout.write("Test map...")
    stdout.flush()
    time2 = timeit.Timer('map(test1, a)', setup=setup).timeit()
    stdout.write("done!\n")

    print("Native:     %fs" % time1)
    print("Map:        %fs" % time2)
    print("Diffenrece: %fs" % abs(time2 - time1))

if __name__ == "__main__":
    test()
