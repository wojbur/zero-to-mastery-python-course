# set comprehension

my_set = {char for char in 'hello'}
print(my_set)

my_set2 = {char.upper() for char in 'hello' if char in 'aeiou'}
print(my_set2)

# dictionary comprehension
simple_dict = {'a':1, 'b':2, 'c':3, 'd':4}
my_dict = {key:value**2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)
