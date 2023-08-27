#include <iostream>
#include <math.h>
#include <string>
#include <cmath>

using namespace std;

int main() {
  int n, a, b;

  cin >> n >> a >> b;

  a = a + b;

  for (int i = 0; i < n; i++) {
    int c;

    cin >> c;

    if (a == c) {
      cout << i + 1 << "\n";
      break;
    }

  }
}
