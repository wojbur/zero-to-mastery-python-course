while True:
    try:
        age = int(input('What is your age? '))
        10/ age
        raise ValueError('hey cut it out')
    except ZeroDivisionError:
        print("age can't be zero")
        break
    else:
        print('thank you')
        break
    finally:
        print('ok, i am finally done')
    print('can you hear me')
