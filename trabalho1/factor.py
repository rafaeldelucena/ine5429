import prime_numbers

class Factor:
    def numberList(self):
        return []
    def getFactor(self, n):
        factors = []
        if n > 1:
            numbers = numberList()
            for number in numbers:
                while((_, divmod(n, number)) == 0):
                    pass
                factors.append(number)
        return factors


class PrimeFactor(Factor):
    def numberList(self):
        return prime_numbers.primeNumbers
