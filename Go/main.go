package main

import "fmt"

func functionName1(parameter1, parameter2, parameter3 int) {
	parameter1 -= parameter2
	parameter3 |= parameter1
	x := 42
	y := x + 10
	if y > 0 {
		fmt.Println("Positive")
	} else if x < 0 {
		fmt.Println("Negative")
	} else {
		fmt.Println("Zero")
	}
}

func functionName2(parameter int) {
	var y int = 52
	y++
	switch parameter {
	case 1:
		fmt.Println("Case 1")
	case 2:
		fmt.Println("Case 2")
	default:
		fmt.Println("Default Case")
	}

	var anotherValue string
	switch anotherValue {
	case "A":
		fmt.Println("Case A")
	case "B":
		fmt.Println("Case B")
	}
}

func functionName3() {
	// Тело функции
}

func outerFunction() {
	outerVariable := 10

	array := []int{}
	for _, item := range array {
		fmt.Println(item)
	}

	for number := 1; number <= 5; number++ {
		fmt.Println(number)
	}

	value := 0
	switch value {
	case 1:
		fmt.Println("Case 1")
	case 2:
		fmt.Println("Case 2")
	default:
		fmt.Println("Default Case")
	}

	innerFunction := func() {
		fmt.Println("Inside innerFunction, outerVariable is:", outerVariable)
	}
	innerFunction()

	result := someFunction("value", 42)
	anotherResult := anotherFunction()
	fmt.Println(result, anotherResult)
}

func generateFibonacci(limit int) []int {
	fibonacciSeries := []int{}
	a, b := 0, 1

	for a <= limit {
		fibonacciSeries = append(fibonacciSeries, a)
		a, b = b, a+b
	}

	c, d := 0, 1
	for {
		nextValue := c + d
		if nextValue > limit {
			break
		}
		fibonacciSeries = append(fibonacciSeries, nextValue)
		c, d = d, nextValue
	}

	x := 42
	y := 3.14
	aa := 42
	fmt.Println(x, y, aa)

	return fibonacciSeries
}

func someFunction(arg1 string, arg2 int) string {
	fmt.Println(arg1, arg2)
	return "result"
}

func anotherFunction() string {
	return "anotherResult"
}

func main() {
	fmt.Println("\n=== Генерация чисел Фибоначчи до 100 ===")
	fibSeries := generateFibonacci(100)
	fmt.Println("Ряд Фибоначчи:", fibSeries)

	functionName3()
}
