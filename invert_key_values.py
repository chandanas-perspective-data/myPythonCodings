def invert(d):
	return {v: k for k, v in d.items()}


print (invert({1: 'a', 2:'b'}))