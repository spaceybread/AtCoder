#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;

int main() {
    
    int n;
    string s;
    
    cin >> n;
    cin >> s;
    
    bool A = false;
    bool B = false;
    bool C = false;
    int i;
    
    while (A == false || B == false || C == false) {
        
        if (s[i] == 'A') {
            A = true;
        }
        if (s[i] == 'B') {
            B = true;
        }
        if (s[i] == 'C') {
            C = true;
        }
        i = i + 1;
        
        
    }
    
    cout << i << "\n";
    
    return 0;
}

