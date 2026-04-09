def multiply_numbers(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply_numbers(2, 4, 1, 2))
