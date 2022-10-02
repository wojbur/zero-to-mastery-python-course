# Unordered collection of unique objects

my_set = {"adam", 1, True, 1, "red", "red"}

print(my_set)

my_set.add(100)
my_set.add("adam")

print(my_set)


# Return list with no duplicates

my_list = [1,2,3,3,4,5,5,6]
my_set = set(my_list)

print(1 in my_set)

my_set2 = my_set.copy()
my_set.clear()

print(my_set)
print(my_set2)