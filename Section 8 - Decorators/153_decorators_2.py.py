# Decorator - function that wraps another funcion and changes it
def my_decorator(func):
    def wrap_func():
        print('****')
        func()
        print('****')
    return wrap_func

@my_decorator
def hello():
    print('helllloooo')

@my_decorator
def bye():
    print('see ya later')

def hey():
    print('hey hey hello')

hey = my_decorator(hey)

# hello()
# bye()
hey()
