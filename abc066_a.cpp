#include <iostream>

using namespace std;

int main() {
  
  int a, b, c;
  
  cin >> a >> b >> c;
  
  int n, m;
  
  if ((a < b) && (a < c)) {
    n = a;
    if (b < c) {
      m = b;
    } else {
      m = c;
    }
    
  } else if ((b < a) && (b < c)) {
    n = b;
    if (a < c) {
      m = a;
    } else {
      m = c;
    }
  } else {
    n = c;
    if (a < b) {
      m = a;
    } else {
      m = b;
    }
  } 
  
  cout << n + m << "\n";
}
