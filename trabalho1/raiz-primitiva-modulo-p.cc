#include <vector>
#include <iostream>
#include <cstdlib>

std::vector<int> gpow, gpowinv;
void CalcGen(long long P){
    gpow.resize(P);
    while(1){
        long long G = rand() % (P - 1) + 1;
        gpow[0] = 1;
        bool ok = true;
        for(int i=1; i<P-1; i++){
            gpow[i] = (long long)(gpow[i-1])*G % P;
            if(gpow[i] == 1){
                ok = false;
                break;
            }
        }
        if(ok) break;
    }
    gpowinv.resize(P);
    for(int i=0; i<P; i++) gpowinv[gpow[i]] = i;
}

int main (int argc, char ** argv)
{
    if (argc != 2) {
        std::cout << "usage: proots <number>\n\n\t<number> must be prime" << std::endl;
    }
    long long number = atoi(argv[1]);
    CalcGen(number); 
    for (unsigned int i =0 ; i < gpow.size(); i++) {
        for (unsigned int j =0 ; j < gpowinv.size(); j++) {
            if (gpow[i] == gpow[j]) {
                std::cout << gpow[i] << std::endl;
            }
        } 
    }
}
