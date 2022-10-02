my_list = [1,2,3,4,5,6,7,8,9,10]

def is_even(num):
    return num % 2 == 0

even_list = list(filter(is_even, my_list))

print(my_list)
print(even_list)
