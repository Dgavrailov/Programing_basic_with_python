budjet = int(input())
season = input()
number_of_fishermens = int(input())
price_for_ship = 0

if season == "Spring":
    price_for_ship = 3000
elif season == "Winter":
    price_for_ship = 2600
else:
    price_for_ship = 4200

if number_of_fishermens <= 6:
    price_for_ship *= 0.9
elif number_of_fishermens <= 11:
    price_for_ship *= 0.85
else:
    price_for_ship *= 0.75

if number_of_fishermens % 2 == 0 and season != "Autumn":
    price_for_ship *= 0.95

total = abs(budjet - price_for_ship)
if budjet > price_for_ship:
    print(f'Yes! You have {total:.2f} leva left.')
else:
    print(f"Not enough money! You need {total:.2f} leva.")