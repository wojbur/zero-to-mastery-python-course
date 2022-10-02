# iterable - object that can be iterated over
# list, dictionary, tuple, set, string...
# iterated -> go one by one to check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.keys():
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for key, value in user.items():
    print(f'key: {key}, value: {value}')
