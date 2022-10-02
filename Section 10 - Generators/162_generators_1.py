# range(100) # elemets created one by one
# list(range(100)) # whole list in memory

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)