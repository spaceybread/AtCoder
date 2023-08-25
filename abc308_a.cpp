#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;

int main() {
    
    int n[8];
    
    for (int i = 0; i < 8; i++) {
        cin >> n[i];
    }
    
    bool flag = true;
    
    for (int i = 1; i < 8; i++) {
        if (n[i] < n[i - 1]) {
            flag = false;
        }
        if (n[i] % 25 != 0) {
            flag = false;
        }
        if (n[i] < 100 || n[i] > 676) {
            flag = false;
        }
    }
    
    if (flag == true) {
        cout << "Yes \n";
    } else {
        cout << "No \n";
    }
    return 0;
}

