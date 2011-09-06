if __name__ == '__main__':
    import sys, timeit

    if len(sys.argv) > 1:
        n=int(sys.argv[1])
    else:
        n=1000

    t=timeit.Timer('countones.countonesiterative(uuid.uuid4().int)','import uuid, countones')
    print "countonesiterative() x %d: %.2f usec/pass" % (n, 1000000 * t.timeit(number=n)/n)
    t=timeit.Timer('countones.countonesrecursive(uuid.uuid4().int)','import uuid, countones')
    print "countonesrecursive() x %d: %.2f usec/pass" % (n, 1000000 * t.timeit(number=n)/n)
    t=timeit.Timer('countones.countonesgenerated(uuid.uuid4().int)','import uuid, countones')
    print "countonesgenerated() x %d: %.2f usec/pass" % (n, 1000000 * t.timeit(number=n)/n)
    t=timeit.Timer('countones.countonesconverted(uuid.uuid4().int)','import uuid, countones')
    print "countonesconverted() x %d: %.2f usec/pass" % (n, 1000000 * t.timeit(number=n)/n)