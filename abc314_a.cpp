#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;

int main() {
    
    string pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
    
    int n;
    cin >> n;
    
    int i = 0;
    
    while (i < n + 2) {
        cout << pi[i];
        i = i + 1;
    }
    cout << "\n";
    return 0;
    
}
