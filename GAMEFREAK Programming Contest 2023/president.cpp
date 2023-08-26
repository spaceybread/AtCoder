// this does not work, I have this here so that I can work on it later

#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    int x[n];
    int y[n];
    int z[n];
    
    int towns[n];
    
    for (int i = 0; i < n; i++) {
        towns[i] = 0;
    }


    int taka = 0;
    int aoki = 0;
    
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i] >> z[i];
        
        if (x[i] > y[i]) {
            taka = taka + z[i];
            towns[i] = 1;
        } else {
            aoki = aoki + z[i];
        }
        
    }
    
    if (taka > aoki) {
        cout << 0 << "\n";
    } else {
        
        int votes = 0;
        
        while (taka < aoki) {
            int maxTown = 0;
            
            
            for (int i = 0; i < n; i++) {
                if ((y[i] - x[i]) <= (y[maxTown] - x[maxTown]) && towns[i] == 0) {
                    maxTown = i;
                }
            }
            
            int delta = (-x[maxTown] + y[maxTown] + 1)/2;

            towns[maxTown] = 1;
            taka = taka + z[maxTown];
            aoki = aoki - z[maxTown];
            
            votes = votes + delta;
            
        }
        cout << votes << "\n";
    }
    
    
    
}
