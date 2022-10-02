# list comprehension: quick way to make list instead of loops

my_list = []

for char in 'hello':
    my_list.append(char.upper())
print(my_list)

# list comprehension:
# [action(param) for param in iterable]
my_list2 = [char.upper() for char in 'hello']
print(my_list2)

my_list3 = [num**2 for num in range(100)]
print(my_list3)

my_list4 = [num**2 for num in range(100) if num % 2 == 0]
print(my_list4)
