class Toy():
    def __init__(self, color, age, height):
        self.color = color
        self.age = age
        self.height = height
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color} toy'

    def __len__(self):
        return self.height

    # def __del__(self):
    #     print('Deleted!')

    def __call__(self):
        return 'yess??'

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0, 25)
print(action_figure.__str__())

print(str(action_figure))

print(len(action_figure))

# del(action_figure)

print(action_figure())

print(action_figure['name'])
