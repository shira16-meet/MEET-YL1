class animal:
	def __init__(self,name,color,age,size):
		self.name=name
		self.color=color
		self.age=age
		self.size=size
	def print_all(self):
		print (self.name)
		print (self.color)
		print (self.age)
		print (self.size)

dog=animal(name='max',color='green',age=99,size='small')
dog.print_all()
