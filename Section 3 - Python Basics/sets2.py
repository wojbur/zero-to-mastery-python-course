# https://www.w3schools.com/python/python_ref_set.asp

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}


# print(my_set.difference(your_set)) #{1,2,3}

# my_set.discard(5) # remove 5 from set
# print(my_set) # {1,2,3,4}

# my_set.difference_update(your_set) # remove all elements of another set from this set
# print(my_set) # {1,2,3}

# print(my_set.intersection(your_set)) # {4,5}
# print(my_set & your_set) #^the same

# print(my_set.isdisjoint(your_set)) # False; are those sets overlaping

# print(my_set.union(your_set)) # {1,2,3,4,5,6,7,8,9,10} connecting sets
# print(my_set | your_set) #^the same

my_set2 = {4,5}
print(my_set2.issubset(your_set)) # True, the entire set2 is in your_set
print(your_set.issuperset(my_set2)) # True