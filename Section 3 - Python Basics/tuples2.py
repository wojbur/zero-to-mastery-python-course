# https://www.w3schools.com/python/python_ref_tuple.asp

x,y,z, *other = (1,2,3,4,5)

print(x)
print(other)


my_tuple = (1,5,3,4,5,5)

print(my_tuple.count(5)) #3
print(my_tuple.index(4)) #3
print(len(my_tuple)) #6