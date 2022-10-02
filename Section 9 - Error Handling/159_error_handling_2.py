def div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(div('1', 2))
print(div(2, 0))
