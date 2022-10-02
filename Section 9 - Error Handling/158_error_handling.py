while True:
    try:
        age = int(input('What is your age? '))
        10/ age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print("age can't be zero")
    else:
        break
