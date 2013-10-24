import math

'''returns the Greatest Common Divisor of a and b'''

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a
