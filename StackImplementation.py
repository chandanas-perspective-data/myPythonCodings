class Stack:	# last-in - first-out

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, element):
		self.items.append(element)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)





x = [238, 389, 84, 389, 893, 23903,3803]

print (type(x))

print (x[0])

x[0] = 3893;

print (x)



# s = Stack()

# print (s.isEmpty())

# s.push("A")
# s.push("B")

# print (s.isEmpty())

# print (s.peek())

# print (s.items)

# print (s.pop())

# print (s.items)



# list1 = []

# print (type(list1))

# list1.append("hi")


# list1.append("hello")

# print (list1)

# list1.append("python")

# print (list1)


# list1.pop()
# print (list1)