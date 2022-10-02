#Dictionary key must be immutable!

dictionary = {
	123: [1,2,3],
	True: 'hello',
	# [100]: True <- this wont work!
}

#Key is usually a string

dictionary2 = {
	'123': [1,2,3],
	'123': 'hello',
}

print(dictionary2['123'])

#key has to be unique, ^ it was overwritten