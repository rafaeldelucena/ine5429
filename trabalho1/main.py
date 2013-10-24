import primitive_root

def main():
    prime = int(input('Enter your prime number: '))
    print "The primitive root of", prime, "is",  primitive_root.primitiveRoot(prime)
main()
