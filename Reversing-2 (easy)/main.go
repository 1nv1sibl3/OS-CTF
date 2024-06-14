package main

import (
	"fmt"
	"os"
)

func checkFlag(flag string) bool {
	// Function that checks if the provided flag is correct
	expectedFlag := "flag{this_is_the_hidden_flag}"
	return flag == expectedFlag
}

func main() {
	fmt.Println("Welcome to the Go Reverse Engineering Challenge!")
	fmt.Println("Can you find the hidden flag?")
	fmt.Print("Enter the flag: ")

	var flag string
	fmt.Scanln(&flag)

	if checkFlag(flag) {
		fmt.Println("Congratulations! You found the correct flag.")
	} else {
		fmt.Println("Sorry, that's not the correct flag. Keep trying!")
		os.Exit(1)
	}
}