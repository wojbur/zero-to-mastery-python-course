# print(True == 1)    #True
# print('' == 1)      #False
# print([] == 1)      #False
# print(10 == 10.0)   #True
# print([] == [])     #True

# == check for equality of values
# == will convert to the same type
# you should copare the same type not to be confusing

# print(True is 1)    #False
# print('' is 1)      #False
# print([] is 1)      #False
# print(10 is 10.0)   #False
# print([] is [])     #False

# 'is' checks if location in memory is the same

# print(True is True)
# print('1' is '1')
# print([] is [])
list1 = [1,2,3]
list2 = list1
list3 = list1.copy()
print(list1 is list2)
print(list1 is list3)