class SuperList(list):
    def __len__(self):
        return 5000

my_list = SuperList([1,2,2,4,1,5,8,3,4,7,12,3,98,22,4,7,9,2,44,1,2,2,3,4,8])

my_list.append(147)
print(my_list.count(2))
print(sorted(my_list))
print(my_list[5])

print(len(my_list))

print(issubclass(SuperList, list))