from random import randint
from sys import argv

range_start = int(argv[1])
range_end = int(argv[2])
random_number = randint(range_start, range_end)
guessed_number = None
while True:
    try:
        guessed_number = int(input(f'Guess a number between {range_start} and {range_end} '))
    except ValueError:
        print('Please enter a number')
    else:
        if guessed_number < range_start or guessed_number > range_end:
            print(f'Hey bozo, I said numbers between {range_start} and {range_end}')
        elif guessed_number != random_number:
            print('You guessed wrong, try again. ')
        else:
            print('Correct!')
            break
