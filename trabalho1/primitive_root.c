#include <gmp.h>
#include <stdio.h>

int main(int argc, char * argv[])
{
    mpz_t prime, phi, index; /* working numbers */
    if (argc<2) { /* not enough words */
        printf("Please supply a prime number.\n");
        return 1;
    }
    mpz_init_set_str (prime, argv[1], 10); /* Assume decimal integers */
    mpz_init_set_ui(index, 2);
    mpz_init(phi);
    mpz_sub_ui(phi, prime, 1); /*phi = prime - 1*/
    for (;mpz_cmp(index, phi) < 0; mpz_add_ui(index, index, 1)) { /* Try all [2 .. phi] */
        mpz_t div;
        mpz_init_set_str(div, "2", 10);
        mpz_t number;
        mpz_init_set(number, phi);
        int is_root = 1;
        while(mpz_cmp_ui(number, 0) != 0) { /* With this loop we find all prime factors of phi*/
            mpz_t one, result2;
            mpz_init(result2);
            mpz_init_set_ui(one, 1);
            mpz_fdiv_r(result2, number, div);
            if(mpz_cmp_ui(result2, 0) != 0) {
                mpz_add_ui(div, div, 1);
            } else {
                mpz_fdiv_q(number, number, div);
                mpz_t exp, result;
                mpz_init(exp);
                mpz_init(result);
                mpz_fdiv_q(exp, phi, div); /* We have the prime factor on div, so calculates phi/prime factor i*/ 
                
                //printf("phi %s\n", mpz_get_str (NULL, 10, phi));
                //printf("factors %s\n", mpz_get_str (NULL, 10, div));
                //printf("base %s\n", mpz_get_str (NULL, 10, index));
                //printf("exp %s\n", mpz_get_str (NULL, 10, exp));
                //printf("mod prime %s\n", mpz_get_str (NULL, 10, prime));

                mpz_powm(result, index, exp, prime); /*a^(phi/prime factor i) mod prime*/
                if (mpz_cmp_ui(result, 1) == 0) { /*if true isnt a primitive root*/
                    is_root = 0;
                }
                if(mpz_cmp_ui(number, 1) == 0) {
                    break;
                }
            }
        }
        if (is_root == 1) {
            printf("The first primitive root founded is %s\n", mpz_get_str (NULL, 10, index));
            return;
        }
    }

    return 0;
}
