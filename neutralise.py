def neutralise(s1, s2):
		return ''.join(a if a == b else '0' for a, b in zip(s1, s2))


print (neutralise("+-9", "+-3"))