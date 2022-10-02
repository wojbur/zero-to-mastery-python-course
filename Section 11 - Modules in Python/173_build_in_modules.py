import random

print(random.random())
print(random.randint(1, 10))
print(random.choice(['apple', 'cherry', 'banana', 'pinaple']))
lst = [1,2,3,4,5,6,7,8,9]
random.shuffle(lst)
print(lst)