basket = ['a', 'b', 'c', 'd', 'e']

print(basket.index('d'))
print(basket.index('c', 0, 3))

print('c' in basket)
print('x' in basket)

print(basket.count('a'))
basket.append('a')
print(basket.count('a'))