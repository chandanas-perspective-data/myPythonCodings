def fizz_buzz(x):
	if x % 3:
		return str(x) if x % 5 else "Buzz"
	return "Fizz" if x % 5 else "FizzBuzz"


print (fizz_buzz(29))