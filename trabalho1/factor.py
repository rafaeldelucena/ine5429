import math
import random
import miller_rabin

def greatestCommonDivisor(u, v):
    while v:
        u, v = v, u % v
    return abs(u)

def pollardFactorize(N):
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
                        g = greatestCommonDivisor(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = greatestCommonDivisor(abs(x-ys),N)
                        if g>1:
                                break
         
        return g


def primeFactors(n, sort = False):
    factors = []
    while n > 1:
        if miller_rabin.probablyPrime(n, 100):
            factors.append(n)
            break
        factor = pollardFactorize(n) 
        factors.extend(primeFactors(factor,sort)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sort: factors.sort()    
    return factors
