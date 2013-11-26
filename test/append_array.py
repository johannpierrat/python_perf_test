#! /usr/bin/python2.7

import timeit

def test():
    code1 = '''
    tab += [None] * 100
    '''

    code3 = '''
    for i in xrange(100):
        tab.append(None)
    '''

    time1 = timeit.Timer(code1, setup="tab = []").timeit()
    time3 = timeit.Timer(code3, setup="tab = []").timeit()

    print "time +=         %fs" % time1
    print "time for append %fs" % time3

if __name__ == "__main__":
    test()
