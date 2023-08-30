#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
  int a, b, k;

  cin >> k >> a >> b;

  bool flag = false;
  
  while (a <= b) {
    if (a % k == 0) {
      flag = true;
      break;
    }
    a = a + 1;
  }

  if (flag == true) {
    cout << "OK \n";
  } else {
    cout << "NG \n";
  }
 
}
