# Higher Order Function HOC:
# function that accepts other function

def greet(func):
    func()

# function that return other funcion
def greet2():
    def func():
        return 5
    return func
