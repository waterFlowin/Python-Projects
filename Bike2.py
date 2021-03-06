class Bike(object):
	def __init__(self, price, max_speed, miles = 0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print self.price
		print self.max_speed
		print self.miles
		return self

	def ride(self):
		print "Riding"
		self.miles += 10
		return self

	def reverse(self):
		print "Reversing"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		return self


bike1 = Bike(200, "25 mph", 0)
bike2 = Bike(100, "15 mph", 0)
bike3 = Bike(50, "10mph", 0)

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()