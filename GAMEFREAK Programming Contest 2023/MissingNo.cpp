#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    int p[n];
    
    int max = 0;
    int min = 1001;
    
    for (int i = 0; i < n; i++) {
        cin >> p[i];
        
        if (max < p[i]) {
            max = p[i];
        }
        
        if (min > p[i]) {
            min = p[i];
        }
        
    }
    
    int check[max];
    
    for (int i = 0; i < max; i++) {
        if (i < min) {
            check[i] = 1;
        }
        else {
            check[i] = 0;
        }
    }
    
    for (int i = 0; i < n; i++) {
        check[p[i]] = 1;
    }
    
    for (int i = 0; i < max; i++) {
        if (check[i] == 0) {
            cout << i <<  "\n";
        }
        
    }
    
    
    
}
