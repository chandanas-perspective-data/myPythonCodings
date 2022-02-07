
# Find the number of digits in a given number
def number_length(num):
  return sum(1 for i in str(num))


print (number_length(10000))