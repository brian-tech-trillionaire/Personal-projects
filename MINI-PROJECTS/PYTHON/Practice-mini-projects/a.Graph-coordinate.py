a = [0, 2, 4, 6, 8, 10]
# Creating two lists, a and b, with different sets of numbers
b = [-1, -4, -3, -6, -5, -8]

# Using the zip() function to combine the two lists a and b into a list of tuples,
# where each tuple contains one element from each list at the corresponding position.
# The resulting list of tuples is stored in the variable zipped.
zipped = list(zip(a, b))
# Printing the list of tuples created by zipping the two lists together.
# Each tuple will contain one element from list a and one element from list b.
# Forming tuples of 2 numbers which we call graph coordinates
print(zipped)
