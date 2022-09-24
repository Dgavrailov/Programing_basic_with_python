budget = float(input())
number_of_videocard = int(input())
number_of_proccesors = int(input())
number_of_ram_memories = int(input())

price_videocards = number_of_videocard * 250
one_price_proccesors = price_videocards * 0.35
price_one_memory = price_videocards * 0.1

needed_price = price_videocards + one_price_proccesors * \
               number_of_proccesors + price_one_memory * \
               number_of_ram_memories
if number_of_videocard > number_of_proccesors:
    needed_price *= 0.85  # otstypka ot 15 %

difference = abs(budget - needed_price)
if budget >= needed_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")