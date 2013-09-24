// Sample program demonstrating the use of the Big Integer Library.

// Standard libraries
#include <string.h>
#include <iostream>
#include <vector>

// `BigIntegerLibrary.hh' includes all of the library headers.
#include "BigIntegerLibrary.hh"

BigInteger powerOf(BigInteger base, BigInteger expo)
{
    if (expo == 0) {
        return 1;
    }
    BigInteger result(1);
    for (BigInteger i = 0; i < expo; i++) {
        result *= base;
    }
    return result;
}


int isPrimitive (BigInteger q, BigInteger a) {
	BigInteger k, s;

	s=1;
    int z;
	BigInteger i=0;

    std::vector<BigInteger> factors;
	while (s>0 && q-2 >= i) {
		k=powerOf(a,i);
		s=k-(q*(k/q));
		for (z=0;z< factors.size();z++) {
			if (factors[z]==s) {
				return 0;
			}
		}
		factors.push_back(s);
		i++;
	}

	if (q-2 == 1) {
		return 1;
	} else {
		return 0;
	}
}

int main (int argc, char **argv) {
    if (argc != 2) {
        std::cout << "usage: sample <prime-number>" << std::endl;
    }
	BigInteger q,a;
    int result;
    std::string s(argv[1]);
	q=stringToBigInteger(s);
	a=stringToBigInteger(s);

	do {
		a--;
		result=isPrimitive(q,a);
	} while (result==0 && a>0);

	if (result==0) {
        std::cout << "Can't find primitive root for " << q << std::endl;
	} else {
        std::cout << a << " is primitive root for " << q << std::endl;
	}
}
