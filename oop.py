class Animal(object):
	def __init__(self,name,age,sound):
		self.name  = name
		self.age = age
		self.sound = sound
		
	def eat(self,food):
		print(self.name + ' is eating' +  food)
	def description(self):
		print(self.name + ' is ' + str(self.age) + ' years old' )
	def make_sound(self):
		for x in range():
			print(self.sound)


dog = Animal("alex",10, 'bark')
dog.description()
dog.eat(' lasagna')
dog.make_sound()



