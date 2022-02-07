def move(word):
	return ''.join(chr(ord(i) + 1) for i in word)


print (move("python"))

print (move("zzz"))

print (chr(ord("A")))