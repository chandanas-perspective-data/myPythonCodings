import math

#print (help(math))
def XpowerY(x,y):
	z = math.pow(y,x)
	if ((z == y) & (x/y  == y)):
		return True;
	else:
		return False;

print (XpowerY(2,1))


x = 38983

print (type(x))

x = 3893.90