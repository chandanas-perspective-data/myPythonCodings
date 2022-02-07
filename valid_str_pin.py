def valid(txt):
    return txt.isnumeric() and len(txt) in [4, 6]


print (valid("4232"))
print (valid("32ad"))

def valid(txt):
  return len(txt) in [4,6] and txt.isdigit()

print (valid("38929"))

from re import match
def valid(txt):
    return bool(match("\d{4}$|\d{6}$", txt))

print (valid("3892"))


def valid(txt):
    return (len(txt) == 4 or len(txt) == 6) and txt.isdigit() and ' ' not in txt


print (valid("389999"))