class User():
    def sign_in(self):
        print('logged it')

# subclasses
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with power of arrows: arrows left {self.num_arrows}')


wizard1 = Wizard('Gandalf', 50)
archer1 = Archer('Tarnum', 85)


print(isinstance(wizard1, Wizard)) # True
print(isinstance(wizard1, User)) # True
print(isinstance(wizard1, object)) # True

