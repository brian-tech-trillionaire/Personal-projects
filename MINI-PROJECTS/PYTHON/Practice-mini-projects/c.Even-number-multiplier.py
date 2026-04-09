evens = list(range(2, 21, 2))

count = 1
for even in evens:
    count *= even
print(f"Multiplication is {count}")
