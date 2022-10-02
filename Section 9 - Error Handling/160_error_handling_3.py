while True:
    try:
        age = int(input('What is your age? '))
        10/ age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print("age can't be zero")
        break
    else:
        print('thank you')
        break
    finally:
        print('ok, i am finally done')
    print('can you hear me')
