def highest_even(nums: list):
    return max((num for num in nums if num % 2 == 0))


def highest_even2(nums: list):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)


print(highest_even([10,1,2,71,3,4,8,17]))
print(highest_even2([10,1,2,71,3,4,8,17]))