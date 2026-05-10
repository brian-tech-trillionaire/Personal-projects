def multiplier(*numbers):
    count = 1
    for number in numbers:
        count *= number
    return count


print(multiplier(1, 3, 4, 4))
