class MathDojo(object):

	def add(self, *nums):
		print nums[0] + nums[1] 
		return self

	def subtract(self, *nums):
		nums - nums
		return self

md = MathDojo()
md.add(1,2)