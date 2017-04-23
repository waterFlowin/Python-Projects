def scores():
	i = 0

	while i < 10:
		print "Enter your test score between 60 and 100"
		score = int(raw_input())
		if score >= 90:
			print "Score:", score, "; Your grade is A"
		elif score >= 80:
			print "Score:", score, "; Your grade is B"
		elif score >= 70:
			print "Score:", score, "; Your grade is C"
		elif score >= 60:
			print "Score:", score, "; Your grade is D"
		i += 1
	print "End of the program. Bye!"

scores()