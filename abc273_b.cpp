#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    long long int x, k, a;
    
    cin >> x >> k;
    
    a = 1;
    
    for (int i = 0; i < k; i++) {
        a = a * 10;
        
        if (10*(x % a)/a >= 5) {
            x = x + a - x % a;
        } else {
            x = x - x % a;
        }
        
    }
  
    cout << x << "\n";
    
}
