

class list_upgrade:

	def __init__(self):
		self.list = []
	
	def append_(self, element):
		self.list.insert(0, element)

	def pop_(self):
		return self.list.pop(0)


l = list_upgrade()
print (l.list)
l.append_(23)
print (l.list)
l.append_("hello")

print (l.list)

l.pop_()
print (l.list)