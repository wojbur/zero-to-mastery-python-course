class User():

    def sign_in(self):
        print('logged it')

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

    def check_arrows(self):
        print(f'{self.num_arrows} remaining')
    
    def run(self):
        print('running fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('borgie', 50, 100)

hb1.run()
hb1.check_arrows()
hb1.attack()
hb1.sign_in()
