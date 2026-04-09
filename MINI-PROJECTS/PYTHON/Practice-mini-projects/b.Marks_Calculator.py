marks = [("Mathematics", 76),
         ("Physics", 85),
         ("Chemistry", 78),
         ("English", 90),
         ("Computer Science", 92)
         ]

prices = [mark[1] for mark in marks]
total_marks = sum(prices)
print(f"Total Marks: {total_marks}")
