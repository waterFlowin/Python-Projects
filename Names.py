### 1111111111111

# name = {
# 	'students' : [ 
# 	     {'first_name':  'Michael', 'last_name' : 'Jordan'},
# 	     {'first_name' : 'John', 'last_name' : 'Rosales'},
# 	     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
# 	     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# 	]
# }

# for key,data in name.items():
# 	for	val in data:
# 		print val['first_name'], val['last_name']





#####2222222222222222

users = {
	'Students': [ 
		{'first_name' : 'Michael', 'last_name' : 'Jordan'},
		{'first_name' : 'John', 'last_name' : 'Rosales'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
	],
}

teach = {
	'Instructors': [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'Martin', 'last_name' : 'Puryear'}
	]
}

for key,data in users.items():
	i = 1
	print "Students"
	for value in data:
		print i, "-", value["first_name"].upper(), value["last_name"].upper(), "-", len(value["first_name"]) + len(value["last_name"])
		i += 1

for key,data in teach.items():
	i = 1
	print "Instructors"
	for value in data:
		print i, "-", value["first_name"].upper(), value["last_name"].upper(), "-", len(value["first_name"]) + len(value["last_name"])		
		i += 1