# square every object
my_list = [5, 4, 3]
print(list(map(lambda x: x**2, my_list)))

# list sorting based on the secend value
a = [(0,2), (4, 3), (9,9), (10, -1)]
print(sorted(a, key= lambda x: x[1]))
