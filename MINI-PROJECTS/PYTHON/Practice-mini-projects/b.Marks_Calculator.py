# Creating a list of tuples called marks, where each tuple contains a subject and its corresponding mark
marks = [("Mathematics", 76),
         ("Physics", 85),
         ("Chemistry", 78),
         ("English", 90),
         ("Computer Science", 92)
         ]

# Using a list comprehension to extract the marks (the second element of each tuple)
# from the marks list and store them in a new list called prices
prices = [mark[1] for mark in marks]
# Printing the list of marks extracted from the marks list
total_marks = sum(prices)
# Printing the total marks by summing up the values in the prices list using the sum() function and formatting the output with an f-string
print(f"Total Marks: {total_marks}")
