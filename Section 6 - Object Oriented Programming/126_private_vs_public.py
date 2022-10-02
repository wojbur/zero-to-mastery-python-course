# we shouldnt have acces to __init__, functions etc. 
# python dont have true private variables
# _attr is convention to let others know it should be private
# __  dunder methods should not be modified

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old')


player1 = PlayerCharacter('andrei', 100)
player1.speak()
