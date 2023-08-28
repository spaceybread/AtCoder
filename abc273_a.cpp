#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
  int n;

  cin >> n;

  int prod = 1;
  
  if (n == 0) {
    prod = 1;
  } else {
    for (int i = 1; i < n+1; i++) {
      prod = prod*i;
    }  
  }

  cout << prod << "\n";
}
