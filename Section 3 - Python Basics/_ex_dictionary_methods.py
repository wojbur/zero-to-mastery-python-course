#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
	'age': 44,
	'username': 'Joahim',
	'weapons': [],
	'is active': True,
	'clan': None
}
#2 iterate and print all the keys in the above user.
print(user.keys())
#3 Add a new weapon to your user
user['weapons'] = ['katana']
user['weapons'].append('shuriken')
#4 Add a new key to include 'is_banned'. Set it to false
user.update({'is_banned': False})
#5 Ban the user by setting the previous key to True
user['is_banned'] = True
#6 create a new user2 my copying the previous user and update the age value and username value. 
user2 = user.copy()
user2['age'] = 24
user2['username'] = 'Hieronim'

print(user)
print(user2)