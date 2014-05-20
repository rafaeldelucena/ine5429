import math
import sys

def bigRange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

def primeFactors(n):
    f, fs = 3, set()
    while n % 2 == 0:
        fs.add(2)
        n /= 2
    while f * f <= n:
        while n % f == 0:
            fs.add(f)
            n /= f
        f += 2
    if n > 1: fs.add(n)
    return fs

def primitiveRoots(number):
    roots = []
    if (number < 2):
        return roots
    phi = number - 1
    factors = primeFactors(phi)
    for m in bigRange(2, phi, 1):
        is_root = True
        for p in factors:
            if pow(m, int(phi / p), number) == 1:
                is_root = False
        if (is_root):
            roots.append(m)
    return roots

def main():
    number = int(raw_input("Enter a prime number: "))
    roots = primitiveRoots(number)
    if (roots):
        print("Find ", len(roots), " primitive roots module ", number, " = ", roots)

if __name__ == "__main__":
    sys.exit(main())
