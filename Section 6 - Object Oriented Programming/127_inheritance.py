# Inheritance allows new objects to take properties of existing objects
# Users:
#   - wizards
#   - archers
#   - ogers etc.


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


gandalf = Wizard('Gandalf', 50)
tarnum = Archer('Tarnum', 85)

gandalf.attack()
tarnum.attack()

gandalf.sign_in()
tarnum.sign_in()
