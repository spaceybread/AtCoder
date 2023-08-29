package main

import ("fmt")

func main() {

  var n, k, x, y int;

  fmt.Scanf("%v", &n);
  fmt.Scanf("%v", &k);
  fmt.Scanf("%v", &x);
  fmt.Scanf("%v", &y);

  var sum int;

  if (n > k) {
    sum = k * x + (n - k) * y;
  } else {
    sum = n * x;
  }

  fmt.Println(sum);
}
