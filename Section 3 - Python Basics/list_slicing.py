amazon_cart = [
	'notebook',
	'glasses',
	'shoes',
	'toys',
	'grapes'
	]

# print(amazon_cart[:2])
# print(amazon_cart[::2])
# print(amazon_cart[::-1])


# amazon_cart[2] = 'boots'
# new_cart = amazon_cart[1:3]
# print(amazon_cart)
# new_cart[1] = 'sunglasses'
# print(new_cart)

new_cart = amazon_cart #new_cart IS amazon cart, not a different list!

new_cart[0] = 'gum'

print(amazon_cart)
print(new_cart)

newer_cart = amazon_cart[:]
new_cart[0] = 'tape'

print(amazon_cart)
print(newer_cart)