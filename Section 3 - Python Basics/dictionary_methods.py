user = {
	'basket': [1,2,3],
	'greet': 'hello'
}


print(user.get('age', 55))

#get(key, default) default will return if key doesnt' exist

# print(user['age']) <- KeyError - it's not added to the dictionary


user2 = dict(name='JonTron') #not very common

print(user2)