class Car(object):

	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()


	def display_all(self):
		if self.price > 10000:
			tax = .15
		else:
			tax = .12
		print "Price:", self.price, "Speed:",self.speed, "Fuel:",self.fuel, "Mileage:",self.mileage, "Tax:",tax


car1 = Car(11000, "180mph","FULL",0)
car2 = Car(9000, "80mph","3/4",0)
car3 = Car(8000, "50mph","it'll get you there",0)
car4 = Car(600, "25mph","some",0)
car5 = Car(0, "5mph","empty",400000)

car1
car2
car3
car4
car5