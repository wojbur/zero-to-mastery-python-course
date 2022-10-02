class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} if running')


player1 = PlayerCharacter('Kevin', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1)
print(player2)
print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)

player1.run()
player2.run()

# player2.attack = 50

# print(player2.attack)
# print(player1.attack)
