
# Adding Two numbers using Lambda function

def adds_n(n):
	return lambda x: x+n

#solution 2
adds_n = lambda n: lambda x: x + n

adds_n = adds_n(1)
print (adds_n(3))