# def sum(num1, num2):
#     return num1 + num2


def sum(num1, num2):
    def another_func(n1, n2):
        return n1+n2
    return another_func(num1, num2)
    print("hello") #this will not be executed, return exits the function



total = sum(5,8)

print(total)