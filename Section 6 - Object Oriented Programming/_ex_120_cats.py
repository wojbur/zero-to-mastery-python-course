#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Maggie', 4)
cat2 = Cat('Bart', 7)
cat3 = Cat('Olaf', 1)
# 2 Create a function that finds the oldest cat
def get_max_age(*args):
    return max(arg.age for arg in args)

def get_oldest_cat(*args):
    for arg in args:
        if arg.age == get_max_age(*args):
            return arg

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {get_max_age(cat1, cat2, cat3)} years old.')

oldest_cat_name = get_oldest_cat(cat1, cat2, cat3).name
oldest_cat_age = get_oldest_cat(cat1, cat2, cat3).age

print(f'The oldest cat is {oldest_cat_name} and is {oldest_cat_age} years old.')
