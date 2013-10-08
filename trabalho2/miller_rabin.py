import random

"""
O número deve ser ímpar
http://rosettacode.org/wiki/Miller-Rabin_primality_test
Devo fatorá-lo em 2^t*s +1 (Todo ímpar é descrito como 2*N+1)
http://home.sandiego.edu/~dhoffoss/teaching/cryptography/10-Rabin-Miller.pdf
"""
def modulo(a,b,c):
        x = 1
        y = a
        while b>0:
                if b%2==1:
                        x = (x*y)%c
                y = (y*y)%c
                b = b/2
        return x%c
         
def millerRabin(N,iteration):
        if N<2:
                return False
        if N!=2 and N%2==0:
                return False
         
        d=N-1
        while d%2==0:
                d = d/2
         
        for i in range(iteration):
                a = random.randint(1, N-1)
                temp = d
                x = modulo(a,temp,N)
                while (temp!=N-1 and x!=1 and x!=N-1):
                        x = (x*x)%N
                        temp = temp*2
                 
                if (x!=N-1 and temp%2==0):
                        return False
         
        return True
"""
import random
 
def decompose(n):
   exponentOfTwo = 0
 
   while n % 2 == 0:
      n = n/2
      exponentOfTwo += 1
 
   return exponentOfTwo, n
 
def isWitness(possibleWitness, p, exponent, remainder):
   possibleWitness = pow(possibleWitness, remainder, p)
 
   if possibleWitness == 1 or possibleWitness == p - 1:
      return False
 
   for _ in range(exponent):
      possibleWitness = pow(possibleWitness, 2, p)
 
      if possibleWitness == p - 1:
         return False
 
   return True
 
def probablyPrime(p, accuracy=100):
   if p == 2 or p == 3: return True
   if p < 2: return False
 
   numTries = 0
   exponent, remainder = decompose(p - 1)
 
   for _ in range(accuracy):
      possibleWitness = random.randint(2, p - 2)
      if isWitness(possibleWitness, p, exponent, remainder):
         return False
 
   return True
"""
