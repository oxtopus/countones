''' Four examples of a function that, given an integer, returns the number of ones in that number's
    binary representation.    
'''

def countonesiterative(n):
    ''' Count ones using an iterative technique
    '''
    c=0
    while n!=0:
        m=n>>1
        c += n-(m<<1)
        n=m
    return c

def countonesrecursive(n):
    ''' Count ones using a recursive technique
    '''
    m=n>>1
    c=n-(m<<1)
    if n > 0:
        return c + countonesrecursive(m)
    else:
        return c

def countonesgenerated(n):
    ''' Count ones using a generator
    '''
    def _(n):
        while n!=0:
            m=n>>1
            yield n-(m<<1)
            n=m
        raise StopIteration

    return len([i for i in _(n) if i])

def countonesconverted(n):
    ''' Count ones by converting to a binary string, and using str.count()
    '''
    return bin(n).count('1')

if __name__ == '__main__':
    import sys
    for n in [int(n) for n in sys.argv[1:]]:
        print n, countonesiterative(n), countonesrecursive(n), countonesgenerated(n), \
            countonesconverted(n)