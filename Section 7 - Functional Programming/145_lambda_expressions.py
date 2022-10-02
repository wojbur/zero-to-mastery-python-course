from functools import reduce

# labmda expressions

# lambda param: action(param)

def multiply_by2(item):
    return item*2

my_list = [1,2,3]

# by using defined function
print(list(map(multiply_by2, my_list)))

# by using lambda param: param * 2
print(list(map(lambda item: item*2, my_list)))

# filter by using lambda
print(list(filter(lambda x: x%2 != 0, my_list)))

# reduce using lambda
print(reduce(lambda a, i: a + i, my_list))

