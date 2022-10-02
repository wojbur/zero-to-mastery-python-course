# iterable - any element that can be iteratet over
# it has __iter__ function
# iterating is taking element from iterable one by one
# generators are iterable

def generator_function(num):
    for i in range(num):
        yield i*2

# yield pauses the funcion

my_generator = generator_function(10000)

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

your_generator = generator_function(1)

print(next(your_generator))
# print(next(your_generator)) # StopIteration