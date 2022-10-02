from collections import Counter, defaultdict, OrderedDict

li = [1,1,2,7,4,4,5,8,4,1,3,2,6,7,5]
sentence = 'blah blah blah, thinking about Python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: None, {'a': 1, 'b': 2})
print(dictionary['a'])
print(dictionary['c'])

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d1)
