type_of_flower = input()
number = int(input())
budget = int(input())
price = 0
if type_of_flower == "Rose":
    price = 5
    if number > 80:
        price *= 0.9
elif type_of_flower == "Daliq":
    price = 3.8
    if number > 90:
        price *= 85
elif type_of_flower == "Tulips":
    price = 2.8
    if number > 80:
        price *= 0.85
elif type_of_flower == "narcis":
    price = 3
    if number < 120:
        price *= 0.15 / 100
elif type_of_flower == "gladiola":
    price = 2.5
    if number < 80:
        price *= 0.2 / 100
total = price * number
diff = abs(budget - total)
if budget > total:
    print(f'"Hey, you have a great garden with \
{number} {type_of_flower} and {diff} leva left."')
else:
    print(f"Not enough money, you need {diff} leva more.")