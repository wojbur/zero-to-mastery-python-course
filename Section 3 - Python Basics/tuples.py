#Tuple - immutable lists

my_tuple = (1,2,3,4,5)

# my_tuple[1] = "z" <- TypeError 

print(my_tuple[3])
print(5 in my_tuple)

#tuples can be used as dictionary keys

user = {
	'age': 44,
	'username': 'Joahim',
	'weapons': [],
	(1,2): True,
	'clan': None
}

print(user[(1,2)])
print(user.items())
