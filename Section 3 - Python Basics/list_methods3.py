basket = ['dog', 'cat', 'rat', 'mice', 'iguana']

print(basket)
basket.sort(reverse=True)
print(basket)

print(sorted(basket))
print(basket)

new_basket = basket.copy()
print(new_basket)
new_basket.reverse()
print(new_basket)