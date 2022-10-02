my_file = open('sample.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(5)
# print(my_file.read())

# my_file.seek(0)
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

print(my_file.readlines())

my_file.close()
