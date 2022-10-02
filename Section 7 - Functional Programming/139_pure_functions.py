# Pure function: given the same input it'll always return the same output
# function should not produce any side effect affecting the outside of scope of function


def multiply_by2(lst: list):
    new_lst = []
    for item in lst:
        new_lst.append(item * 2)
    return new_lst

def attack(character):
    return f'attacking with the power of {character["power"]}'


wizard = {
    'name': 'Merlin',
    'power': 50
}

print(attack(wizard))


print(multiply_by2([1,2,3]))
