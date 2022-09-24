budget = float(input())
num_of_nights = int(input())
price_of_night = float(input())
percent_for_extra_taxes = int(input())

if num_of_nights > 7:
    price_of_night *= 0.95
    total_night = price_of_night * num_of_nights
elif num_of_nights <= 7:
    total_night = price_of_night * num_of_nights

percent_for_extra_taxes = budget * (percent_for_extra_taxes / 100)

total_vacation = total_night + percent_for_extra_taxes
total = abs(budget - total_vacation)
if total_vacation <= budget:
    print(f"Ivanovi will be left with {total:.2f} leva after vacation.")
else:
     print(f"{total:.2f} needed.")