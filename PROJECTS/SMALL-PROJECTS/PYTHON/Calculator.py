import math as m


def Sum(a, b):
    return a + b


def Difference(a, b):
    return a - b


def Products(a, b):
    return a * b


def Division(a, b):
    if b == 0:
        return None
    else:
        return a/b


def Power(a, b):
    return m.power(a, b)


def Sin(a):
    return m.sin(a)


def Sin_2(b):
    return m.sin(b)


def Cos(a):
    return m.cos(a)


def Cos_2(b):
    return m.cos(b)


def Tan(a):
    return m.tan(a)


def Tan_2(b):
    return m.tan(b)


while True:
    a = float(input('a:'))
    b = float(input('b:'))

    Choice = input("Put your choice:")
    if Choice == 'Sum':
        print(round(Sum(a, b), 2))

    if Choice == 'Difference':
        print(round(Difference(a, b), 2))

    if Choice == 'Product':
        print(round(Products(a, b), 2))

    if Choice == 'Power':
        print(round(Power(a, b), 2))

    if Choice == 'Sin(a)':
        print(round(Sin(a), 2))

    if Choice == 'Sin(b)':
        print(round(Sin_2(b), 2))

    if Choice == 'Cos(a)':
        print(round(Cos(a), 2))

    if Choice == 'Cos(b)':
        print(round(Cos_2(b), 2))

    if Choice == 'Tan(a)':
        print(round(Tan(a), 2))

    if Choice == 'Tan(b)':
        print(round(Tan_2(b), 2))

    if Choice == 'Division':
        print(round(Division(a, b), 2))

    Division = Division(a, b)
    if Division == None:
        'Error: Cannot be divided by zero'
    else:
        Division(a, b)

    if Choice == 'Division':
        print(round(Division, 2))

    if b > 20:
        break
