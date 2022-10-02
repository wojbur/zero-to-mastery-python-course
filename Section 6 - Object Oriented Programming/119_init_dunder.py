'''
__init__ is called every time new object is istancianted
'''

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='annon', age=0):
        if (age >= 18):
            self.name = name
            self.age = age

    def run(self, distance: int):
        print(f'{self.name} if running the distance of {distance}km')
        return 'done'
    
    def shout(self):
        print(f'MY NAME IS {self.name.upper()}')


player1 = PlayerCharacter('Tom', 10)

player1.shout() # <- error, the player was 'name' was not created because 10<18
