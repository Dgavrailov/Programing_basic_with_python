beverage = input()
sugar = input()
number_of_drinks = int(input())

suma = 0
total = 0

if beverage == "Espresso":
    if sugar == "Without":
        suma = 0.9 * 0.65
    elif sugar == "Normal":
        suma = 1
    elif sugar == "Extra":
        suma = 1.2
    if number_of_drinks >= 5:
        total = suma * 0.75 * number_of_drinks
    else:
        total = suma * number_of_drinks

if beverage == "Cappuccino":
    if sugar == "Without":
        suma = 1 * 0.65
    elif sugar == "Normal":
        suma = 1.2
    elif sugar == "Extra":
        suma = 1.6
    total = suma * number_of_drinks

if beverage == "Tea":
    if sugar == "Without":
        suma = 0.5 * 0.65
    elif sugar == "Normal":
        suma = 0.6
    elif sugar == "Extra":
        suma = 0.7
    total = suma * number_of_drinks

if total >= 15:
    total *= 0.8

print(f'"You bought {number_of_drinks} cups of {beverage} for {total:.2f} lv."')