class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged it')
    

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with power of arrows: arrows left {self.num_arrows}')


wizard1 = Wizard('Jeneffer', 130, 'jeneffer87@gmail.com')

# introspection - ability to determine the type of the object at runtime

print(dir(wizard1))
