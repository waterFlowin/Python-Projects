##11111111111111111


# def draw_stars(arr):
# 	for i in arr:
# 		print "*" * i


# draw_stars([4,6,1,3,5,7,25])


##22222222222222222

def draw_stars(arr):
	idx = 0
	while idx < len(arr):
		if isinstance(arr[idx], int):
			print "*" * arr[idx]
		elif isinstance(arr[idx], str):
			print arr[idx][0] * len(arr[idx])
		idx += 1

draw_stars([4,6,1,'string',5,7,25])