class Animal:
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
	def eat(self,food):
		print (self.name + " is eating", food)
	def sleep(self):
		print (self.name+" is sleeping")

raccoon=Animal(name='max',color='green',age=99,size='small')
raccoon.print_all()
raccoon.eat("bone")
raccoon.sleep()

panda=Animal(name="po",color="black and white",age=10,size='big')
panda.print_all()
panda.eat("leaf")
panda.sleep()
