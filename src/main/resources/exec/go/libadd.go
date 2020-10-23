//libadd.go
package main

import "C"
import "fmt"

//export add
func add(left, right int) int {
	return left + right
}
//export saySomething
func saySomething(){
	fmt.Println("Hello, World!")
}

func main() {
}
