# *args **kwargs


# Rule: params, *args, default params, **kwargs
def super_func(name, *args, i='hi', **kwargs):
    # print(args)
    # print(kwargs)
    return sum(args) + sum(kwargs.values())



print(super_func('Andy', 1,2,3,4,5, num1=5, num2=10))

