import math

def _onRange(start, stop, inc):
    while start < stop:
        yield start
        start += inc

def primeFactors(n):
    factors = []
    number = abs(n)
    factor = 2

    while number > 1:
        factor = getNextPrimeFactor(number, factor)
        factors.append(factor)
        number /= factor

    if n < -1: # If we'd check for < 0, -1 would give us trouble
        factors[0] = -factors[0]

    return factors

def getNextPrimeFactor(n, f):
    if n % 2 == 0:
        return 2

# Not 'good' [also] checking non-prime numbers I guess?
# But the alternative, creating a list of prime numbers,
# wouldn't it be more demanding? Process of creating it.
    for x in _onRange(max(f, 3), int(math.sqrt(n) + 1), 2):
        if n % x == 0:
            return x

    return n



def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

def primeFacs(n):
    primes = rwh_primes2((n/2)+1)
    return [x for x in primes if n%x == 0]

import random
import gcd
def brent(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:            
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd.gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd.gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g


import miller_rabin
def bigfactors(n, sort = False):
    factors = []
    while n > 1:
        if miller_rabin.probablyPrime(n, 100):
            factors.append(n)
            break
        factor = brent(n) 
        factors.extend(bigfactors(factor,sort)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort: factors.sort()    
    return factors
