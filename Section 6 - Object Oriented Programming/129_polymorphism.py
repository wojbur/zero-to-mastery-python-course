# polymorphism -> object classes can share the same method name and act differently based on what object is called

class User():
    def sign_in(self):
        print('logged it')
    
    def attack(self):
        print('no power attack')

# subclasses
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with power of arrows: arrows left {self.num_arrows}')


wizard1 = Wizard('Gandalf', 50)
archer1 = Archer('Tarnum', 85)

def player_attack(char):
    char.attack()

# The same fucntion give different result
player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
