user = {
	'basket': [1,2,3],
	'greet': 'hello',
	'age': 20
}

# print('basket' in user)
# print('weight' in user)

# print(20 in user.keys())
# print('greet' in user.keys())

# print(20 in user.values())
# print('greet' in user.values())

# print(user.items())

# user.clear()
# print(user)

# user2 = user.copy()
# print(user is user2)

# print(user.pop('age'))
# print(user)

# print(user.popitem()) # removes the last added to dictionary

user.update({'age': 55})
print(user)