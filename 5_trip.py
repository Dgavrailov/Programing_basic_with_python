budget = float(input())
season = input()
price = 0
destination = str
type_of_sleep = str
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.7
    elif season == "winter":
        price = budget * 0.3
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.6
    if season == "winter":
        price = budget * 0.2
if budget > 1000:
    destination = "Europe"
    if season == "summer":
        price = budget * 0.1
    if season == "winter":
        price = budget * 0.1

total = (budget - price)

if season == "summer":
    type_of_sleep = "Camp"
else:
    type_of_sleep = "Hotel"

print(f'Somewhere in {destination}')
print(f'{type_of_sleep} - {total:.2f}')