#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int n, h, x;
    
    cin >> n >> h >> x;
    
    int p[n];
    
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }
    
    x = x - h;
    
    for (int i = 0; i < n; i++) {
        if (p[i] >= x) {
            cout << i + 1 << "\n";
            break;
        }
    }
}
