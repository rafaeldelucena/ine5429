#include <iostream>
#include <string>
#include <inttypes.h>

typedef uint16_t word;
using namespace std;

word nibbleSub(word w)
{
    return w;
}

word shiftRow(word w)
{
    return w;
}

word mixColumn(word w)
{
    return w;
}

word keyAddition(word w)
{
    return w;
}

typedef word (*aes_func)(word);

aes_func pipeline[] = {
    nibbleSub, shiftRow, mixColumn, keyAddition, 0
};

int main()
{
    word input, output;
    cout << "Digite um Nibble" << endl;
    cin >> input;
    aes_func* ptr = pipeline;
    while (*ptr != 0) {
        aes_func f;
        f = *ptr;
        output = f(input);
        ptr++;
    }
    cout << "Saida " << output << endl;
    
    return 0;
}
