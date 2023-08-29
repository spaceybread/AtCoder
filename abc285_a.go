package main
import ("fmt")

func main() {
  var i,j int;
  fmt.Scanf("%v %v",&i, &j);

  if (i * 2 == j || i * 2 + 1 == j) {
    fmt.Println("Yes");

  } else {
    fmt.Println("No");
  }

}
