def atbash(txt):
	a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
	z = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
	s = ''
	for i in txt:
		if i in a:
			s += z[a.index(i)]
		else:
			s += i
	return s


print (atbash("hello"))

# method 2

from string import ascii_letters as alpha

def atbash(txt):
	return txt.translate(str.maketrans(alpha, alpha[::-1].swapcase()))

print (atbash("python"))

# method 3

def atbash(txt):
  return ''.join(chr(219 - ord(i)) if i.islower() else chr(155 - ord(i)) if i.isupper() else i for i in txt)

print (atbash("ab"))