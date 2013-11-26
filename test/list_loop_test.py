#!/usr/bin/python2.7

import timeit
import sys

def test():
    setup = "import random\na = random.sample(xrange(1000), 100)"

    code1 = '''
    b = []
    for i in a:
        b.append(i)
    '''

    code3 = '''
    b = []
    map(b.append, a)
    '''

    stdout = sys.stdout
    stdout.write("test 1: simple...")
    stdout.flush()
    time1 = timeit.Timer(code1, setup=setup).timeit()
    stdout.write("done!\n")
    stdout.write("test 2: array...")
    stdout.flush()
    time2 = timeit.Timer('b = [i for i in a]', setup=setup).timeit()
    stdout.write("done!\n")
    stdout.write("test 3: map...")
    stdout.flush()
    time3 = timeit.Timer(code3, setup=setup).timeit()
    stdout.write("done!\n")
    print("simple loop: %fs" % time1)
    print("array loop:  %fs" % time2)
    print("map loop:    %fs" % time3)

if __name__ == "__main__":
    test()
