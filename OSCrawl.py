import os

def walk(dirname):
	names = []
	print (os.listdir(dirname))
	for each in os.listdir(dirname):
		path = os.path.join(dirname, each)
		print (path)

		if os.path.isfile(path):
			print (os.path.isfile(path))
			names.append(each)
			#print (each)
		else:
			names.extend(walk(path))
	return names

walk("C:/Users/Harish/Downloads")

import string
print (string.punctuation)