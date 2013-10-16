def primeFactors (number):
    factors = []
    if number > 1:
        primes = primeList()
        for prime in primes:
            quotient, remainder = divmod(number, prime)
            if remainder == 0:
                while(_, divmod(quotient, number) == 0):
                factors.append(prime)
        composites = compositeList()
        for composite in composites:
            quotient, remainder = divmod(number, composite)
            if remainder == 0:
                while(_, divmod(quotient, number) == 0):
                factors.append(composite)
    return factors

def primitiveRoot (number):
    phi = number - 1
    factors = primeFactors(phi)
    for m in range(number - 1, 1):
        for p in factors:
            if pow(m, phi / p, number) == 1:
                return m
    return -1
