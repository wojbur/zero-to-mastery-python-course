# Scope - what variables do I have acces to?

def some_func():
    total = 100

if True:
    x = 10


# print(total) # NameErros <- total not in scope
print(x)