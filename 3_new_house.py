type_flower = input
number_of_flower = int(input())
budjet = int(input())
price_of_flower = 0

if type_flower == "Roses":
    price_of_flower = 5
    if number_of_flower > 80:
        price_of_flower *= 0.9 # price per flower = price per flower * 0.9
elif type_flower == "Dahlias":
    price_of_flower = 3.8
    if number_of_flower > 90:
        price_of_flower *= 0.85
elif type_flower == "Tulips":
    price_of_flower = 2.8
    if number_of_flower > 80:
        price_of_flower *= 0.85
elif type_flower == "Narcissus":
    price_of_flower = 3
    if number_of_flower < 120:
        price_of_flower *= 1.15
elif type_flower == "Gladiolus":
    price_of_flower = 2.5
    if number_of_flower < 80:
        price_of_flower *= 1.20
total_price = price_of_flower * number_of_flower

difference = abs(budjet - total_price)# kakvoto i da e chisloto shte e polojitelno
if total_price <= budjet:
    print(f'Hey, you have a great garden with {number_of_flower} {type_flower} and {difference:.2f} leva left.')
if total_price > budjet:
    print(f"Not enough money, you need {difference:.2f} leva more.")

