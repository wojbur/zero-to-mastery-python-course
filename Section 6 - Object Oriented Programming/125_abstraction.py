# Abstraction -> hiding information from user and giving accec to only what's necessay

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('andrei', 100)
player1.speak() # <- user dont need to know how the speak() work

player1.name = '!!!'
player1.speak = 'BOO'

print(player1.speak()) # <- error, speak has been modified, overrited, that's bad