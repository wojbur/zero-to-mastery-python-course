from ast import pattern
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

str = 'b@b.com'
str2 = 'z#b.com'

a = pattern.search(str)
print(a)
b = pattern.search(str2)
print(b)