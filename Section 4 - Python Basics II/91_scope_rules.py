a = 1

def parent():
    a = 10
    def confusion():
        return a
    return confusion()


print(a) #  1
print(parent()) # 10
print(a) # 1


#1 - statrs is variable is in local scope
#2 - is there a parent local scope
#3 - global scope
#4 - built in python funcions