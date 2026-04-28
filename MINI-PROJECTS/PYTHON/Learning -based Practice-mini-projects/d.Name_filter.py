names = ["Brian", "Alvin", "Rose", "Esther",
         "Tim", "Linda", "Jeff", "John", "Stacey",]  # Creating a list of names

# Using a list comprehension to filter the names list and create a new list called filtered that contains only the name "Brian"
filtered = [name for name in names if name == "Brian"]
# Printing the filtered list, which will contain only "Brian" if it is present in the original names list, or an empty list if "Brian" is not found.
print(filtered)
