import rsa

if __name__=='__main__':
    bits = int(raw_input("Give the size of random number in bits: "))
    precision = int(raw_input("Which precision to test primality? "))
    message = raw_input("Which message to be used? ")
    (n, e, d) = rsa.generateKeys(bits, precision)
    print ('n = {0}'.format(n))
    print ('Public Key e = {0}'.format(e))
    print ('Private Key d = {0}'.format(d))
    cipher = rsa.encrypt(message, n, e, len(message))
    print(cipher)
    Amessage = rsa.decrypt(cipher, n, d, len(message))
    print(Amessage)
