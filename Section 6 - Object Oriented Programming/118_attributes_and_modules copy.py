'''
class object attributes do not change accross instances of object
class attributes are specific to every instance
'''

class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def run(self, distance: int):
        print(f'{self.name} if running the distance of {distance}km')
        return 'done'
    
    def shout(self):
        print(f'MY NAME IS {self.name.upper()}')


player1 = PlayerCharacter('Kevin', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.membership)
print(player2.membership)

player1.shout()
player2.run(50)
