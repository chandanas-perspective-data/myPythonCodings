class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, element):
		self.items.insert(0, element)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def reverse(self):
		return self.items.reverse()

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")

print (q.items)

q.reverse()
print (q.items)

q.dequeue()

q.dequeue()
print (q.items)

# Realtime : printing tasks are first-in-first-out basis