import math
import sys

"""
Funcao necessaria para criacao de limites com numeros grandes
"""
def bigRange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
"""
Dado um valor de entrada N, retorna uma colecao de fatores primos
"""
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

"""
Dao um numero primo P, encontra os fatores primos de P - 1 e calcula a condicao para raiz primitiva modulo P de um numero A entre 2 ate P - 1.
"""
def primitiveRoots(number):
    roots = []
    if (number < 2):
        yield []
    phi = number - 1
    for m in bigRange(2, phi, 1):
        is_root = True
        for p in primeFactors(phi):
            if pow(m, int(phi / p), number) == 1:
                is_root = False
        if (is_root):
            yield m

if __name__ == "__main__":
    number = int(raw_input("Enter a prime number: "))
    for g in primitiveRoots(number):
        print "Find a primitive root module", number, " = ", g 
        next = raw_input("Find next? (y/N) ")
        if next != ("y" or "Y"):
            sys.exit();
