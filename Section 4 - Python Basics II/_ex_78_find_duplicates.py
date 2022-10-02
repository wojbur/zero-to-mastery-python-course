some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = set()
for letter in some_list:
    if some_list.count(letter) > 1:
        duplicates.add(letter)
print(list(duplicates))


duplicates = []
for letter in some_list:
    if letter not in duplicates:
        if some_list.count(letter) > 1:
            duplicates.append(letter)
print(duplicates)

duplicates = list({letter for letter in some_list if some_list.count(letter) > 1})
print(duplicates)