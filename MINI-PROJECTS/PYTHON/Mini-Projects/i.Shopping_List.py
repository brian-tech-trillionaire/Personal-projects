Shopping_items = ["Milk", "Bread", "Eggs", "Butter", "Cheese"]
items = (0, Shopping_items)
index, Shopping_items = items
for index, item in enumerate(Shopping_items):
    if item == 'Milk':
        price = 60
    elif item == 'Bread':
        price = 65
    elif item == 'Eggs':
        price = 30
    elif item == 'Butter':
        price = 200
    else:
        price = 250

    print(index + 1, item, price)
