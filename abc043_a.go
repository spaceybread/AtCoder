package main

import ("fmt")

func main() {

  var n float64;

  fmt.Scanf("%v", &n);

  var sum float64;

  n = n + 1;
  sum = (n/2.0)*(n - 1.0);

  fmt.Println(sum);
}
