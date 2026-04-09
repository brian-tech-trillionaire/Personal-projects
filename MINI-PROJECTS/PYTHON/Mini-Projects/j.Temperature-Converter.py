def C_to_F(cel):
    return (cel * 9/5) + 32


def F_to_C(fah):
    return (fah - 32) * 5/9


def C_to_K(cel):
    return cel + 273


def K_to_C(kel):
    return kel - 273


while True:
    Converter = float(input('Convert :'))

    Choice = input('Choice?')

    if Choice == 'Cel-to-Fah':
        print(round(C_to_F(cel=Converter), 2))

    if Choice == 'Fah-to-Cel':
        print(round(F_to_C(fel=Converter), 2))

    if Choice == 'Cel-to-Kel':
        print(round(C_to_K(cel=Converter), 2))

    if Choice == 'Kel-to-Cel':
        print(round(K_to_C(kel=Converter), 2))
