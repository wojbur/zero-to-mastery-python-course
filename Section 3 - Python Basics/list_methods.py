# https://www.w3schools.com/python/python_ref_list.asp

basket = [1,2,3,4,5]

#adding
basket.append(6)
print(basket)

basket.insert(2, 2.5)
print(basket)

basket.extend([7,8,9,10])
print(basket)

#removing
basket.pop(0) #index
print(basket.pop())
print(basket)

basket.remove(2.5) #value
print(basket)

basket.clear()
print(basket)