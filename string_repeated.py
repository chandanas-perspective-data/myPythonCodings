
# Check if string is related in same string
def repeated(s):
  return s in (s + s)[1: -1]


print (repeated("hehe"))


print (("hehe"+"hehe")[1:-1])

s = "hehehehe"

print (s[1:-1])