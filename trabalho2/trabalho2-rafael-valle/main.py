#!/usr/bin/python
import random
import miller_rabin

def checkIsPrime():
    number = raw_input("Give some number to check if is prime: ")
    precision = raw_input("Which precision?: ")
    if miller_rabin.probablyPrime(int(number), int(precision)):
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
    while (miller_rabin.probablyPrime(random_number, precision) == False):
        random_number = random.getrandbits(bits)
    print "\tThe random number probably prime is: ", random_number, "\n\n"

if __name__ == '__main__':
    print("---- Miller Rabin Primality Test ----")
    functions = {
            'prime':checkIsPrime,
            'random':generateRandomPrime
            }
    
    while (1):
        print ("Typing random: will try generates a random until is prime")
        print ("Typing prime: will tests a number passed by user\n")
        type = raw_input("Type random or prime: ")
        if type not in functions.keys():
            print ("Invalid choice!")
            continue
        functions[type]()
