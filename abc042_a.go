package main

import ("fmt")

func main() {

  var a, b, c int;

  fmt.Scanf("%v %v %v", &a, &b, &c);

  var sum int;

  sum = a + b + c;


  if ((a == 5 || b == 5 || c == 5) && (a == 7 || b == 7 || c == 7)) {
    if (sum == 17) {
      fmt.Println("YES");
    } else {
      fmt.Println("NO");
    }
  } else {
    fmt.Println("NO");
  }



}
