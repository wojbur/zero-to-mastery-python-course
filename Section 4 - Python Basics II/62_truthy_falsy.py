# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

print(bool(5))
print(bool(0))
print(bool('sample text'))
print(bool(''))
print(bool(['sample list']))
print(bool([]))
print(bool({'sample': 'dict'}))
print(bool({}))
print(bool(1))

print(bool(0))
print(bool(None))
print(bool(()))
print(bool(set()))


username = 'Johny_Kapahala'
password = 'LoveToSurf87'

if password and username:
    print('correct')
else:
    print('not correct')
