class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print self.health, self.name
		return self

animal = Animal("chimp")
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self, name):
		self.name = name
		self.health = 150
	
	def pet(self):
		self.health += 5
		return self

doggy = Dog('Bud')
doggy.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		self.name = name
		self.health = 170
		super(Dragon, self).displayHealth()
		print "this is a dragon!"

	def fly(self):
		self.health -= 10
		return self

dragon1 = Dragon('dro')
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth().displayHealth()