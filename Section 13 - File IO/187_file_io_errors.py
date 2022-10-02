try:
    with open('sad.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as err:
    print('file does not exist')
except IOError as err:
    print('IO error')