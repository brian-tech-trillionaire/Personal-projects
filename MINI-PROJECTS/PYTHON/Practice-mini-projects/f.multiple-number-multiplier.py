# This function takes a variable number of arguments (numbers) and multiplies them together.
def multiply_numbers(*numbers):
    # Initialize the result variable to 1 (the identity for multiplication)
    result = 1
    for number in numbers:        # Iterate through each number in the numbers tuple
        # Multiply the current number with the result and update the result variable
        result *= number
    return result               # Return the final result of the multiplication


# This line calls the multiply_numbers function with the arguments 2, 4, 1, and 2, and prints the result of the multiplication. The expected output is 16 (2 * 4 * 1 * 2 = 16).
print(multiply_numbers(2, 4, 1, 2))
