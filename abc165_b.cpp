#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
  long long int x;
  cin >> x;

  long long int init = 100;

  long long int i = 0;

  while (x > init) {
    init = init/100 + init;
    i++;
  }

  cout << i << "\n";
  
}
