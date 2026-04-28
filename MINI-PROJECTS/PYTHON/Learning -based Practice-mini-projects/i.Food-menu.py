# Importing the deque class from the collections module
from collections import deque
Food_menu = deque()  # Creating an empty deque called Food_menu
Food_menu.append("Greens")  # Adding "Greens" to the right end of the deque
Food_menu.append("Meat")  # Adding "Meat" to the right end of the deque
Food_menu.append("Dessert")  # Adding "Dessert" to the right end of the deque
Food_menu.append("Drinks")  # Adding "Drinks" to the right end of the deque
print("Food_menu:", Food_menu)
print("Removed Greens:", Food_menu.popleft())  # Removing Greens from the queue
print("Food_menu:", Food_menu)
print("Removed Meat:", Food_menu.popleft())  # Removing Meat from the queue
print("Food_menu:", Food_menu)
# Removing Dessert from the queue
print("Removed Dessert:", Food_menu.popleft())
print("Food_menu:", Food_menu)
print("Removed Drinks:", Food_menu.popleft())  # Removing Drinks from the queue
print("Food_menu:", Food_menu)

# Checking if Food_menu is empty
if not Food_menu:
    print("Food menu is empty")
else:
    print("Food menu is not empty")
