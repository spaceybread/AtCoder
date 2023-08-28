#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int n;
    
    cin >> n;
    
    char things[n][12];
    
    for (int i = 0; i < n; i++) {
        cin >> things[i];
    }
    
    for (int i = n - 1; i != -1; i--) {
        cout << things[i] << "\n";
    }
    
}
