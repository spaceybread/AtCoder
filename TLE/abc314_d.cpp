#include <iostream>
#include <math.h>
#include <string>
#include <cmath>
 
using namespace std;

int main() {
    
    int n, q, t, x, j;
    string s;
    char c;
    
    cin >> n;
    cin >> s;
    cin >> q;
    
    
    for (int i = 0; i < q; i++) {
        cin >> t >> x >> c;
        
        if (t == 1) {
            s[x - 1] = c;
        }
        else if (t == 2) {
            for (j = 0; j < n; j++){
                s[j] = tolower(s[j]);
            }
        }
        else if (t == 3) {
            for (j = 0; j < n; j++){
                s[j] = toupper(s[j]);
            }
        }
    }
    cout << s << "\n";
    
    return 0;
}

