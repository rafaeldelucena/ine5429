import factor

def primitiveRoot (number):
    phi = number - 1
    factors = factor.primeFactors(phi)
    for m in range(phi, 0, -1):
        for p in factors:
            if pow(m, int(phi / p), number) != 1:
                return m
    return -1
