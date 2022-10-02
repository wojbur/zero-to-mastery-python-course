with open('test.txt', 'w') as my_file:
    text = my_file.write('hey you')
    print(text)

with open('test.txt', 'a') as my_file:
    text = my_file.write('\nsecond line')
    print(text)

with open('app\sad.txt', 'r') as my_file:
    text = my_file.readlines()
    print(text)

with open('./app/sad.txt', 'r') as my_file:
    text = my_file.readlines()
    print(text) 