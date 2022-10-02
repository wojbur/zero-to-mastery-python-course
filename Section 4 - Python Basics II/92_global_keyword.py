total = 0

def counter():
    global total
    total += 1
    return total

def counter2(total):
    total += 1
    return total


print(counter2(counter2(counter2(counter2(total)))))