
package main
import ("fmt")

func main() {
  var a, b, c int;
  fmt.Scanf("%v %v %v",&a, &b, &c);

  if (b/a >= c) {
    fmt.Println(c);

  } else {
    fmt.Println(b/a);
  }

}
