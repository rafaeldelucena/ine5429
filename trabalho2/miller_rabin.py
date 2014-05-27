import random
import sys

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

def generateRandomPrime():
    bits = int(raw_input("Give the size of random number in bits: "))
    if bits < 2:
        print("\tMust be 2 bits or more!\n")
        return
    precision = int(raw_input("Which precision to test primality? "))
    random_number = random.getrandbits(bits)
    while (probablyPrime(random_number, precision) == False):
        random_number = random.getrandbits(bits)
    print "\tThe random number probably prime is: ", random_number, "\n\n"

def main():
    print("---- Miller Rabin Primality Test ----")
    functions = {
            'prime':checkIsPrime,
            'random':generateRandomPrime,
            'exit':sys.exit
            }
    
    while (1):
        print ("Type random will try generates a random or prime for check if is prime\n")
        type = raw_input("Choose random, prime or exit: ")
        if type not in functions.keys():
            print ("Invalid choice!")
            continue
        functions[type]()

if __name__ == '__main__':
    main()
