#!/usr/bin/python2.7

import timeit
import sys

def test():
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


    stdout = sys.stdout
    stdout.write("test if...")
    stdout.flush()
    time1 = timeit.Timer(code1, setup='a = [10]*100').timeit()
    stdout.write("done!\n")
    stdout.write("Test try...")
    stdout.flush()
    time2 = timeit.Timer(code2, setup='a = [10]*100').timeit()
    stdout.write("done!\n")

    print("with if  %fs" % time1)
    print("with try %fs" % time2)

if __name__ == "__main__":
    test()
