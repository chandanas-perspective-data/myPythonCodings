
# List of multiples of first element with second element consecutive times.
def list_of_multiples (num, length):
	return [i*num for i in range(1,length+1)]


print (list_of_multiples(5,5))


# solution 2

def list_of_multiples (num, length):
	lst = []
	for i in range(length):
		lst.append(num+i*num)
	return lst

print (list_of_multiples(10,2))