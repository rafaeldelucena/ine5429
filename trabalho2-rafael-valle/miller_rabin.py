import random

"""
Decompoe um numero par na forma (2^r) * s
"""
def _decomposeBaseTwo(n):
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
def _fillPrimeConditions(candidateNumber, p, exponent, remainder):
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
   exponent, remainder = _decomposeBaseTwo(p - 1)
 
   for _ in range(accuracy):
      candidateNumber = random.randint(2, p - 2)
      if _fillPrimeConditions(candidateNumber, p, exponent, remainder):
         return False
 
   return True

