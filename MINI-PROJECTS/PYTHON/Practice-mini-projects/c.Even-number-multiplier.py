# Creating a list of even numbers from 2 to 20 using the range function with a step of 2
evens = list(range(2, 21, 2))

count = 1                  # Initializing a variable called count to 1, which will be used to store the result of multiplying the even numbers together
for even in evens:               # Iterating through each even number in the evens list
    count *= even           # Multiplying the current even number with the count variable and updating the count variable with the new value
# Printing the final result of multiplying all the even numbers together using an f-string to format the output
print(f"Multiplication is {count}")
