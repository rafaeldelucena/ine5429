import random
import sys
import math
import time

"""
Decompoe um numero par na forma (2^r) * s
"""
def decomposeBaseTwo(n):
    exponentOfTwo = 0
    while n % 2 == 0:
      n = n/2
      exponentOfTwo += 1
 
    return exponentOfTwo, n

"""
Verifica as condicoes
    Se (a^s === 1 (mod n) ou a^2js === -1 (mod n) 
    para um j | 0 <= j <= r-1
"""
def fillPrimeConditions(candidateNumber, p, exponent, remainder):
   candidateNumber = pow(candidateNumber, remainder, p)
 
   if candidateNumber == 1 or candidateNumber == p - 1:
      return False
 
   for _ in range(exponent):
      candidateNumber = pow(candidateNumber, 2, p)
 
      if candidateNumber == p - 1:
         return False
 
   return True
 
"""
  O numero randomico a na faixa que inicia em 2 pois, o teste 1^s = 1(mod n)
  Seria uma tentavia inutil
"""
def probablyPrime(p, accuracy=100):
   if p == 2 or p == 3: return True
   if p < 2: return False
 
   numTries = 0
   exponent, remainder = decomposeBaseTwo(p - 1)
 
   for _ in range(accuracy):
      candidateNumber = random.randint(2, p - 2)
      if fillPrimeConditions(candidateNumber, p, exponent, remainder):
         return False
 
   return True


def checkIsPrime():
    number = int(raw_input("Give some number to check if is prime: "))
    if (number == 1):
        print("\n\tOne is prime!\n")
        sys.exit()
    precision = raw_input("Which precision?: ")
    if (probablyPrime(number, int(precision))):
        print "\n\tThe number is probably prime!\n"
    else:
        print "\n\tThis is a compose number!\n"

def generateRandomPrime(bits, precision):
    random_number = random.getrandbits(bits)
    while (probablyPrime(random_number, precision) == False):
        random_number = random.getrandbits(bits)
    return random_number


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
    if number:
        if number == 2:
            yield 1
        if number == 3:
            yield 2
        phi = number - 1
        factors = primeFactors(phi)
        for m in bigRange(2, phi, 1):
            is_root = True
            for p in factors:
                if pow(m, int(phi / p), number) == 1:
                    is_root = False
            if (is_root):
                yield m

def diffie_helmann(bits, precision):
    start = time.time()
    prime = generateRandomPrime(bits, precision)
    time_prime = time.time() - start
    print "prime", prime
    print "generateRandomPrime:", time_prime 
    for root in primitiveRoots(prime):
        print "primitive root:", root
        if root == 2:
            break
        XA = random.getrandbits(bits - 1)
        XB = random.getrandbits(bits - 1)
        YA = pow(root, XA, prime)
        YB = pow(root, XB, prime)

        K1 = pow(YB, XA, prime)
        K2 = pow(YA, XB, prime)

        print "Prime P", prime,
        print "Primitive Root Mod P", root
        print "Private Keys XA:", XA, "and XB:", XB
        print "Public Keys YA:", YA, "and YB:", YB
        print "K1:", K1, "K2:", K2
        return


def main():
    bits = int(sys.argv[1])
    #bits = int(raw_input("Give the size of random number in bits: "))
    #precision = int(raw_input("Which precision to test primality? "))
    precision = int (sys.argv[2])
    start = time.time()
    diffie_helmann(bits, precision)
    total = time.time() - start
    print "Total time:", total 

if __name__ == '__main__':
    main()
