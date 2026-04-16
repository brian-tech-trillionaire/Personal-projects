# This code defines a function called users that takes in keyword arguments and returns them as a dictionary. The function is then called with three keyword arguments: name, age, and country, and the resulting dictionary is printed.
def users(**diction):
    return diction


print(users(name="Brian", age=25, country="Kenya"))
