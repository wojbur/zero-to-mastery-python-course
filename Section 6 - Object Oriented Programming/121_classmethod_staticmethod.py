class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'MY NAME IS {self.name.upper()}')
    
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1+num2)
    
    # staticmethod dont have acces to cls
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2



# player1 = PlayerCharacter('Tom', 20)

# classmethods can be used without instanciacing object
player3 = PlayerCharacter.adding_things(20,44)
print(player3.age)
