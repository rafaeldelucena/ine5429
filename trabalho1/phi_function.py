import gcd

def totient(phi):
    number_of_gcds_equal_to_1 = 0
    for positive_integers_less_than_phi in range(phi - 1,0,-1):
        the_gcd = gcd.gcd(phi,positive_integers_less_than_phi)
        if the_gcd == 1:
            number_of_gcds_equal_to_1 += 1
    return number_of_gcds_equal_to_1
 
