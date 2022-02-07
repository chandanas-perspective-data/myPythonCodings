
# Define a function that returns If multiplied First two parameter values and 
#resulted value of last digit equals to third element
def last_dig(a, b, c):
  return str(a*b)[-1] == str(c)[-1]


print (last_dig(12,2, 4))

print (last_dig(32,23,34))