# Instance variable and Instance method

class student:
	def __init__(self): # This is a special method called constructor
		self.name='spandana'
		self.rollno=101
		self.age=23
		self.marks=500
	def room(self): # This is an instance method
		print('Hi I am ',self.name)
		print('My roll no is ',self.rollno)
		print('My age is',self.age)
		print('My marks are',self.marks)
s1=student() # create  an instance to student class
s1.room()  # call the method using the instance
