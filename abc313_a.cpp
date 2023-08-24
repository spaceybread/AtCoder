#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    int people[n];
    
    int i = 0;
    int max = 0;
    int maxInd;
    
    while (i < n) {
        cin >> people[i];
        if (people[i] >= max) {
            max = people[i];
            maxInd = i;
        }
        i = i + 1;
    }
    
    
    if (maxInd == 0) {
        cout << 0 << "\n";
    } else {
        cout << (max - people[0] + 1) << "\n";
    }
    
    return 0;
    
}
