import factor
import random

def primitiveRoot(n):
    if n == 2:
        return 1
    for i in _onRange(2, n):
        if _isPrimitiveRoot(i, n):
            return i
    return None

def _onRange(start, stop):
    while start < stop:
        yield start
        start += 1

def _isPrimitiveRoot(a, p):    
    for f in factor.primeFactors(p-1):
        if pow(a,int((p-1)/f), p) == 1:  
            return False
    return True
