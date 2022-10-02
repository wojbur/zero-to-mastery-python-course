from ast import pattern
import re

pattern = re.compile(r"([a-zA-Z]).([a])")
text = 'this search inside of this text please'

a = pattern.search(text)
print(a)
print(a.group(1))
print(a.group(2))
