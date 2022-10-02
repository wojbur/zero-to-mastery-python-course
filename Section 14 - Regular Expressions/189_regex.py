from ast import pattern
import re

pattern = re.compile('this')

text = 'this search inside of this text please'

# print('search' in text)

a = pattern.search(text)
b = pattern.findall(text)
c = pattern.fullmatch(text)
d = pattern.match(text)
print(a)
print(b)
print(c)
print(d)