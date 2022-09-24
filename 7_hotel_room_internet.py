month = input()
nights = int(input())

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65

    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        studio_rent *= 0.7
        apartment_rent *= 0.9
    elif 7 < nights < 14:
        studio_rent *= 0.95

elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.7
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights
    if nights > 14:
        apartment_rent *= 0.8

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    studio_rent = studio_price * nights
    apartment_rent = apartment_price * nights

    if nights > 14:
        apartment_rent *= 0.9

print(f'Apartment: {apartment_rent:.2f} lv.')
print(f"Studio: {studio_rent:.2f} lv.")
