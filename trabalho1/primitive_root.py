import factor
import random
import phi_function

def primitiveRoot (number):
    phi = phi_function.totient(number)
    if _isPrimitiveRoot(phi, number):
        return phi

def _isPrimitiveRoot(a, p):    
    for f in factor.primeFactors(p-1):
        if pow(a,int((p-1)/f), p) == 1:  
            return False
    return True
