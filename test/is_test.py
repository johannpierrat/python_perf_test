#!/usr/bin/python2.7

import timeit

def test():
    print("Comparing == and 'is' for None evaluation")
    time1 = timeit.Timer('a == None', setup='a = None').timeit()
    time2 = timeit.Timer('a is None', setup='a = None').timeit()
    print("with '==': %fs" % time1)
    print("with 'is': %fs" % time2)

    print("Comparing != and 'is not' for None evaluation")
    time1 = timeit.Timer('a != None', setup='a = None').timeit()
    time2 = timeit.Timer('a is not None', setup='a = None').timeit()
    print("with '!=':     %fs" % time1)
    print("with 'is not': %fs" % time2)

    print("Comparing == and 'is' for True evaluation")
    time1 = timeit.Timer('a == True', setup='a = True').timeit()
    time2 = timeit.Timer('a is True', setup='a = True').timeit()
    print("with '==': %fs" % time1)
    print("with 'is': %fs" %time2)

    print("Comparing != and 'is not' for True evaluation")
    time1 = timeit.Timer('a != True', setup='a = True').timeit()
    time2 = timeit.Timer('a is not True', setup='a = True').timeit()
    print("Result:")
    print("with '!=':     %fs" % time1)
    print("with 'is not': %fs" % time2)

if __name__ == "__main__":
    test()
