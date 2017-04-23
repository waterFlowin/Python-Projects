import random

def coinToss():
	i = 0
	attempt = 0
	h = 0
	t = 0
	while i < 5001:
		random_num = random.random()
		if round(random_num) >= 0.5:
			print "Attempt #",attempt,": Throwing a coin... It's a head! ... Got",h,"head(s) so far and",t,"tail(s) so far"
			attempt += 1
			h += 1
		elif round(random_num) < 0.5:
			print "Attempt #",attempt,": Throwing a coin... It's a tail! ... Got",h,"head(s) so far and",t,"tail(s) so far"
			attempt += 1
			t += 1
		i += 1


coinToss()