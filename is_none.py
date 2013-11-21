#!/usr/bin/python2.7

import timeit

print("Comparing == and 'is' for None evaluation")
time1 = timeit.Timer('a == None', setup='a = None').timeit()
time2 = timeit.Timer('a is None', setup='a = None').timeit()
print("Result:")
print("with '==': %fs\nwith 'is': %fs\ndifference %fs\n"
        % (time1, time2, abs(time2 - time1)))

print("Comparing != and 'is not' for None evaluation")
time1 = timeit.Timer('a != None', setup='a = None').timeit()
time2 = timeit.Timer('a is not None', setup='a = None').timeit()
print("Result:")
print("with '!=': %fs\nwith 'is not': %fs\ndifference %fs\n"
        % (time1, time2, abs(time2 - time1)))

print("Comparing == and 'is' for True evaluation")
time1 = timeit.Timer('a == True', setup='a = True').timeit()
time2 = timeit.Timer('a is True', setup='a = True').timeit()
print("Result:")
print("with '==': %fs\nwith 'is': %fs\ndifference %fs\n"
        % (time1, time2, abs(time2 - time1)))

print("Comparing != and 'is not' for True evaluation")
time1 = timeit.Timer('a != True', setup='a = True').timeit()
time2 = timeit.Timer('a is not True', setup='a = True').timeit()
print("Result:")
print("with '!=': %fs\nwith 'is not': %fs\ndifference %fs"
        % (time1, time2, abs(time2 - time1)))
