#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int n;
    
    cin >> n;
    
    int ponts[n];
    
    for (int i = 0; i < n; i++) {
        cin >> ponts[i];
    }
    
    int maxIn = 0;
    
    for (int i = 0; i < n; i++) {
        if (ponts[i] > ponts[maxIn]) {
            maxIn = i;
        }
    }
    
    cout << maxIn + 1 << "\n";
    
}
